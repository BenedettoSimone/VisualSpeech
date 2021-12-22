from flask import Flask
import webbrowser

app = Flask(__name__)


@app.route('/')
def index():
    return "hello"


@app.route('/main')
def index1():

    webbrowser.open('https://www.apple.com')

if(__name__)=='__main__':
    app.run(host='0.0.0.0', port=80)
