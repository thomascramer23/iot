from sense_hat import SenseHat
import time
sense = SenseHat()
from datetime import datetime

import paho.mqtt.client as mqtt  #import the client1
broker_address="127.0.0.1"
client = mqtt.Client()
def on_connect(client, userdata, flags, rc):
    m="Connected flags: " + str(flags) + " result code: " + str(rc) + " client1_id: " + str(client)
    print(m)

import json

city = "Madrid"
x = 1

while True:
    client.on_connect = on_connect
    client.connect(broker_address, 1883, 60)
    client.loop_start()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    humidity = sense.get_humidity()
    obj = {
    "Humidity is": humidity,
    }
    json_data = json.dumps(obj)
    if(humidity > 50):
        sense.clear([0, 0, 0])
        time.sleep(1)
        client.publish("ETSIDI/Hum",json_data) # Publicamos
        sense.clear([255, 255, 255])
        print(json_data)
        time.sleep(1)
    client.disconnect()
    client.loop_stop()
    x += 1
    time.sleep(2)