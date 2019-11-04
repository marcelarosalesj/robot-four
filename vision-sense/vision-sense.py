import zmq
import time
import cv2

context = zmq.Context()
socket = context.socket(zmq.PUSH)
address = "tcp://0.0.0.0:5557"
socket.bind(address)
print("Sending to {}...".format(address))

cont = 0
while True:
    file_name = '/image-storage/img{}.jpg'.format(cont)
    cont = cont + 1
    image_json = {"path": file_name}
    socket.send_json(image_json)
    print("Sent message")
    time.sleep(1)
