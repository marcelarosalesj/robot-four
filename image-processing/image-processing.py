import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
address = "tcp://vision-sense:5557"
socket.connect(address)
print("Listening to {}...".format(address))

images = [
    {
        'id': 1,
        'path': u'../storage/img01.jpg',
        'path-bw': u'../storage/img01-bw.jpg',
    },
    {
        'id': 2,
        'path': u'../storage/img02.jpg',
        'path-bw': u'../storage/img02-bw.jpg',
    }
]

while True:
    message = socket.recv_json()
    orig_path = message['path']
    bw_path = orig_path.split('.jpg')[0] + '-bw.jpg'
    print('path {}\nbw_path {}\n'.format(orig_path, bw_path))
    print("Client got message! {}".format(message))
    image = {
        'id': images[-1]['id'] + 1,
        'path': message['path'],
        'path-bw': bw_path,
    }
    images.append(image)
    print(images)
