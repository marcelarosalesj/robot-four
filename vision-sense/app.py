import requests

#
# TO-DO: get an image, store it in ../image-storage then call to image-processing/bw
#


# /image-processing/images
resp = requests.get('http://localhost:5000/image-processing/images')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /image-processing/images/ {}'.format(resp.status_code))
for todo_item in resp.json()['images']:
    print('{} {} {}'.format(todo_item['id'], todo_item['path'], todo_item['path-bw']))


# /image-processing/bw
image = {"path": "../image-storage/img04.jpg"}
resp = requests.post('http://localhost:5000/image-processing/bw', json=image)
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Convert image. ID: {}'.format(resp.json()["image"]['id']))

# /image-processing/images
resp = requests.get('http://localhost:5000/image-processing/images')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /image-processing/images/ {}'.format(resp.status_code))
for todo_item in resp.json()['images']:
    print('{} {} {}'.format(todo_item['id'], todo_item['path'], todo_item['path-bw']))
