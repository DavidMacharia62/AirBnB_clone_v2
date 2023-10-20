#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', methods=['GET'])
def hello_airbnb():
    """ Function called with / route """
    return "Hello, from Airbnb onepage!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
