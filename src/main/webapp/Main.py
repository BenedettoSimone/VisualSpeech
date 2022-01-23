import os
from src.main.webapp.Lip_Extractor import lip_extractor
from Plot_image import plot_image
from RemoveImage import remove_image, replicate_last
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


@app.route('/mainENGL', methods=['GET', 'POST'])
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
    num_frames = lip_extractor(FILE_OUTPUT)

    if num_frames <= 49:
        replicate_last(num_frames)

    else:
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


@app.route('/mainITA', methods=['GET', 'POST'])
def index12():
    req1 = request.get_data()

    FILE_OUTPUT = 'video.mp4'

    # Checks and deletes the output file
    if os.path.isfile(FILE_OUTPUT):
        os.remove(FILE_OUTPUT)

    out_file = open(FILE_OUTPUT, "wb")  # open for [w]riting as [b]inary
    out_file.write(req1)
    out_file.close()

    # extract lips from video frame
    num_frames = lip_extractor(FILE_OUTPUT)

    if num_frames <= 49:
        replicate_last(num_frames)

    else:
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
    app.run(host='0.0.0.0', port=80, debug=True)
    # extract lips from video frame

    '''
    
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    for i in range(0, 10):
        print(str(i) + '.mp4')
        num_frames = lip_extractor(str(i) + '.MOV')

        if num_frames <= 49:
            replicate_last(num_frames)

        else:
            # remove similar images
            remove_image()

        # remove similar images
        #remove_image()

        # plot image
        plot_image()
        if (i < 5):
            os.rename('test.png', 'BS_Word_' + str(array[i]) + '_07.png')
        else:
            os.rename('test.png', 'BS_Phrases_' + str(array[i]) + '_07.png')

        '''
# https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451
