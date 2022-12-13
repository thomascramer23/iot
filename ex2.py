from sense_hat import SenseHat
import time
sense = SenseHat()
from datetime import datetime

while True:
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    dew = temperature - (100 - humidity) / 5
    

    print(humidity)
    time.sleep(1)
    