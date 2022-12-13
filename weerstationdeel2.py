import http.client
import urllib
import time
from sense_hat import SenseHat
sense = SenseHat()

import paho.mqtt.publish as publish
import psutil
import string

from flask import Flask
import datetime

app = Flask(__name__)

channel_ID = "1974879"

mqtt_host = "mqtt3.thingspeak.com"

mqtt_client_ID = "MxoZJDEPGS0kEwQfHhgMAjk"
mqtt_username  = "MxoZJDEPGS0kEwQfHhgMAjk"
mqtt_password  = "/4/0tHQhSBgFKbejy4QZH/bJ"

t_transport = "websockets"
t_port = 80

topic = "channels/" + channel_ID + "/publish"

while (True):
    temp = sense.get_temperature()
    hum = sense.get_humidity()
    pres = sense.get_pressure()

    payload = "Temperature=" + temp + "&humidity=" + humidity

    try:
        print ("Writing Payload = ", payload," to host: ", mqtt_host, " clientID= ", mqtt_client_ID, " User ", mqtt_username, " PWD ", mqtt_password)
        publish.single(topic, payload, hostname=mqtt_host, transport=t_transport, port=t_port, client_id=mqtt_client_ID, auth={'username':mqtt_username,'password':mqtt_password})
    except (keyboardInterrupt):
        break
    except Exception as e:
        print (e)


@app.route("/get/temperature")
def getTemperature():
   temp = sense.get_temperature()
   return "Current temperature is: " + temp

@app.route("/get/humidity")
def getHumidity():
   humidity = sense.get_humidity()
   return "Current humidity is: " + humidity

@app.route("/get/pressure")
def getPressure():
   pressure = sense.get_pressure()
   return "Current air pressure is: " + pressure

@app.route("/get/all")
def getPressure():
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    return "Current temperature is: " + temp + ", current humidity is: " + humidity + ", current air pressure is: " + pressure

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)