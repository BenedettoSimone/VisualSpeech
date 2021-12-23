from flask import Flask, jsonify, request, render_template, make_response
import webbrowser

app = Flask(__name__)


@app.route('/')
def index():
    return "hello"


    #return render_template("http://localhost:8080/VisualSpeech_war_exploded/prova.html", a)

@app.route('/main', methods=['GET','POST'])
def index1():
    req = request.get_json()
    print(req)

    res = make_response(jsonify({"message":"JSON received"}), 200)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'

    return res


@app.route("/parameter/<a>")
def index2(a):
    return '<h1>' + a + '<h1>'


@app.route("/response", methods=['GET', 'POST'])
def index3():
    dataGet = request.get_json(force=True)
    print(dataGet)

    dataReply = {'this': 'that'}
    return jsonify(dataReply)


if (__name__) == '__main__':
    app.run(host='0.0.0.0', port=80)



#https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451