import os

import cv2
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)


@app.route('/main', methods=['GET', 'POST'])
def index1():
    req = request.get_json()
    print(req)

    res = make_response(jsonify({"message": "JSON received"}), 200)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'

    return res


@app.route('/main1', methods=['GET', 'POST'])
def index11():
    req = request.get_data()

    print(req)
    FILE_OUTPUT = 'My-File.mp4'

    # Checks and deletes the output file
    # You cant have a existing file or it will through an error
    if os.path.isfile(FILE_OUTPUT):
        os.remove(FILE_OUTPUT)

    out_file = open(FILE_OUTPUT, "wb")  # open for [w]riting as [b]inary
    out_file.write(req)
    out_file.close()

    vidcap = cv2.VideoCapture('My-File.mp4')
    success, image = vidcap.read()
    count = 0

    # create new directory for frame
    dirname = 'frame'
    os.mkdir(dirname)

    while success:
        cv2.imwrite(os.path.join(dirname, "frame-%d.jpg" % count), image)  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

    res = make_response(jsonify({"message": "Video Received"}), 200)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'

    print(res)
    return res


if (__name__) == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

# https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451
