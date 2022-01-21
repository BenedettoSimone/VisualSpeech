import os
from src.main.webapp.Lip_Extractor import lip_extractor
from Plot_image import plot_image
from RemoveImage import remove_image
from Predict import predict
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

    FILE_OUTPUT = 'video.mp4'

    # Checks and deletes the output file
    if os.path.isfile(FILE_OUTPUT):
        os.remove(FILE_OUTPUT)

    out_file = open(FILE_OUTPUT, "wb")  # open for [w]riting as [b]inary
    out_file.write(req)
    out_file.close()

    # extract lips from video frame
    threshold = lip_extractor(FILE_OUTPUT)


    # remove similar images
    remove_image()

    # plot image
    plot_image()

    response = predict()

    # set response
    res = make_response(jsonify({"message": response}), 200)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'

    print(res)
    return res


if (__name__) == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=True)
    # extract lips from video frame

    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    for i in range(0, 10):
        print(str(i) + '.mp4')
        lip_extractor(str(i) + '.mp4')

        # remove similar images
        remove_image()

        # plot image
        plot_image()
        if (i < 5):
            os.rename('test.png', 'DS_Word_' + str(array[i]) + '_13.png')
        else:
            os.rename('test.png', 'DS_Phrases_' + str(array[i]) + '_13.png')

# https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451