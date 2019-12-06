import zmq
import cv2
import requests
import influxdb
import datetime

# Create socket for ZMQ messaging
context = zmq.Context()
socket = context.socket(zmq.PUSH)
address = "tcp://0.0.0.0:5557"
socket.bind(address)
print("Sending to {}...".format(address))

# Create cap object for USB web camera input
cap = cv2.VideoCapture(0)

# Create DB client object
host = 'database'
port = '8086'
user = 'root'
password = 'root'
dbname = 'images'
http_proxies = {'http': None, 'https': None,
                'http_proxy': None, 'https_proxy': None,
                'HTTP_PROXY':None, 'HTTPS_PROXY':None}
client = influxdb.InfluxDBClient(host=host,
                        port=port,
                        username=user,
                        password=password,
                        database=dbname,
                        proxies=http_proxies)


cont = 0
while True:
    ret, img = cap.read()
    cv2.imshow('Camera', img)
    k = cv2.waitKey(1)
    if k == 27: # ESC
        print('ESC')
        break
    elif k == 115: # [s] shoot
        print('shoot-store-process')
        file_name = '/storage/img{}.jpg'.format(cont)
        cv2.imwrite(file_name, img)
        cont = cont + 1
        # Send to image-processing
        image_json = {"path": file_name}
        socket.send_json(image_json)
        print("Sent message")
        # Send to database
        json_body = [
            {
                "measurement": "camera_capture",
                "tags": {
                    "host": "robot-four",
                    "region": "mex-west"
                },
                "time": str(datetime.datetime.utcnow()),
                "fields": {
                    "image_path": file_name,
                }
            }
        ]
        print("Write points: {0}".format(json_body))
        try:
            client.write_points(json_body)
            print('Write to database complete.')
        except:
            print('ERROR')
    elif k == 100: # [d] display
        query = 'select * from camera_capture;'
        try:
            result = client.query(query)
            print("Query results: {}".format(result))
        except:
            print('ERROR')

cap.release()
cv2.destroyAllWindows()
