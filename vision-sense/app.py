import requests
import cv2

def list_images():
    """
    /image-processing/images
    """
    resp = requests.get('http://r4-ip:8080/image-processing/images')
    if resp.status_code != 200:
        # This means something went wrong.
        raise Exception('GET /image-processing/images/ {}'.format(resp.status_code))
    for todo_item in resp.json()['images']:
        print('{} {} {}'.format(todo_item['id'], todo_item['path'], todo_item['path-bw']))


print("starting vision-sense app")

list_images()

cap = cv2.VideoCapture(0)
cont = 0

while(True):
    ret, img = cap.read()

    cv2.imshow('Camera', img)

    k = cv2.waitKey(1)
    if k == 27: # ESC
        print('ESC')
        break
    elif k == 115: #s
        print('shoot-store-process')
        file_name = '/image-storage/img{}.jpg'.format(cont)
        cv2.imwrite(file_name, img)
        cont = cont + 1
        image = {"path": file_name}
        resp = requests.post('http://r4-ip:8080/image-processing/bw', json=image)
        if resp.status_code != 201:
            raise Exception('POST /tasks/ {}'.format(resp.status_code))
        print('Convert image. ID: {}'.format(resp.json()["image"]['id']))

cap.release()
cv2.destroyAllWindows()

list_images()

print("finishing vision-sense app")
