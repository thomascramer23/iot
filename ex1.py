from sense_hat import SenseHat
import time
sense = SenseHat()
from datetime import datetime

import json

city = "Madrid"

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    temperature = sense.get_temperature()
    obj = {
    "time": current_time,
    "city": city,
    "temperature": temperature,
    }
    json_data = json.dumps(obj)

    print(json_data)
    time.sleep(1)
    