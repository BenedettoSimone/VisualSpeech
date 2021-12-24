import os
from flask import Flask, jsonify, request,make_response

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
    #print(req)

    res = make_response(jsonify({"message": "Video Received"}), 200)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'

    print(res)
    return res

if (__name__) == '__main__':
    app.run(host='0.0.0.0', port=80)

# https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451
