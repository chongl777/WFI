import os

from flask import Flask
from flask import request
import json


app = Flask(__name__, static_url_path="/static")


@app.route('/index')
def index():
    with open('./index.html') as f:
        txt = f.read()
        return txt


@app.route('/submit')
def submit():
    data = request.args['name']
    return "Hello " + data + "!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9999)
