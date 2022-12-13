import http.client
import urllib
import time
from sense_hat import SenseHat

sense = SenseHat()

# API KEY
key = "YL1YIZDN7M9R34TW"  # Put your API Key here

while True:
    temp = sense.get_temperature()
    hum = sense.get_humidity()
    pres = sense.get_pressure()
    
    # Body: data to send
    params = urllib.parse.urlencode({'field1': temp, 'field2': hum, 'field3': pres, 'key':key })
    
    # Headers
    headers = {"Content-type": "application/x-www-form-urlencoded"}

    # Create the connection
    conn = http.client.HTTPConnection("api.thingspeak.com:80")

    # Make the request: GET, POST, DELETE
    conn.request("POST", "/update", params, headers)

    # Get the response
    response = conn.getresponse()

    # Print the response
    print(response.status, response.reason)
    data = response.read()
    print (data)
    
    time.sleep(20)
    


# Close the connection
conn.close()