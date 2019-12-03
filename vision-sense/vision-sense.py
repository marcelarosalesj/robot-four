import zmq
import cv2

context = zmq.Context()
socket = context.socket(zmq.PUSH)
address = "tcp://0.0.0.0:5557"
socket.bind(address)
print("Sending to {}...".format(address))

cap = cv2.VideoCapture(0)

cont = 0
while True:
    ret, img = cap.read()
    cv2.imshow('Camera', img)
    k = cv2.waitKey(1)
    if k == 27: # ESC
        print('ESC')
        break
    elif k == 115: # s
        print('shoot-store-process')
        file_name = '/storage/img{}.jpg'.format(cont)
        cv2.imwrite(file_name, img)
        cont = cont + 1
        image_json = {"path": file_name}
        socket.send_json(image_json)
        print("Sent message")

cap.release()
cv2.destroyAllWindows()
