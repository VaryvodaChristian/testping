import requests
import time
import datetime as dt

request = requests.get("http://54.179.182.131:8000/01/sensor01")

file = open("sensorRequest.txt", "a")

while True:
    time.sleep(1)
    request = requests.get("http://54.179.182.131:8000/01/sensor01")
    now = dt.datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    text = "\nTime: " + formatted + ":" + request.text
    file.write(text)
    print(text)
    

    
    