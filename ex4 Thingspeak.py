#!/usr/bin/python3
import http.client
import urllib
import time

# API KEY
key = "YL1YIZDN7M9R34TW"  # Put your API Key here

# Body: data to send
params = urllib.parse.urlencode({'field1': 25, 'field2': 33, 'key':key })

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

# Close the connection
conn.close()