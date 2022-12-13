from sense_hat import SenseHat
import time
sense = SenseHat()
from datetime import datetime
import paho.mqtt.client as mqtt  #import the client1
broker_address="127.0.0.1"
client = mqtt.Client()
import json

def on_connect(client, userdata, flags, rc):
    m="Connected flags: " + str(flags) + " result code: " + str(rc) + " client1_id: " + str(client)
    print(m)

while True:
    client.on_connect = on_connect
    client.connect(broker_address, 1883, 60)
    client.loop_start()
    temperature = sense.get_temperature()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    temperature = sense.get_temperature()
    obj = {
    "time": current_time,
    "city": "Madrid",
    "temperature": temperature,
    }
    json_data = json.dumps(obj)
    if(temperature < 22):
        sense.clear([0, 0, 0])
        time.sleep(1)
        client.publish("ETSIDI/ID",json_data) # Publicamos
        sense.clear([255, 255, 255])
        time.sleep(1)
    client.disconnect()
    client.loop_stop()
    time.sleep(1)
    
