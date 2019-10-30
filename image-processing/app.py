from flask import Flask, jsonify, abort, make_response, request, url_for

app = Flask(__name__)

images = [
    {
        'id': 1,
        'path': u'../image-storage/img01.jpg',
        'path-bw': u'../image-storage/img01-bw.jpg',
    },
    {
        'id': 2,
        'path': u'../image-storage/img02.jpg',
        'path-bw': u'../image-storage/img02-bw.jpg',
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error' : 'Not found'}), 404)

@app.route('/image-processing/bw', methods=['POST'])
def convert_black_and_white():
    if not request.json or not 'path' in request.json:
        abort(400)
    #
    # TO-DO: Convert image to black and white and store it in ../image-storage
    #
    path_bw = request.json['path']
    path_bw = path_bw.split('.jpg')
    path_bw = path_bw[0] + "-bw.jpg"
    image = {
        'id': images[-1]['id'] + 1,
        'path': request.json['path'],
        'path-bw': path_bw,
    }
    images.append(image)
    return jsonify({'image': image}), 201

@app.route('/image-processing/images', methods=['GET'])
def get_images():
    return jsonify({'images': images})

if __name__ == '__main__':
    app.run(debug=True)
