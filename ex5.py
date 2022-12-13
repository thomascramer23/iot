from flask import Flask
from sense_hat import SenseHat
from flask import request
import time

import datetime
sense = SenseHat()

app = Flask(__name__)

@app.route("/orientation", methods=['POST'])
def setWhite():
    degree = request.form['degree']
    sense.clear([255, 255, 255])
    return degree

@app.route("/black", methods=['POST'])
def setBlack():
    degree = request.form['degree']
    sense.clear([0, 0, 0])
    return degree