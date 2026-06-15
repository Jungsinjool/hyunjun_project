#!/usr/bin/python3

import os
import RPi.GPIO as GPIO
from urllib.parse import parse_qs

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)

print("Content-type: text/html\n")

qString = os.environ.get('QUERY_STRING', '')
qVal = parse_qs(qString)

request = qVal.get('action', [''])[0]

if request.upper() == 'ON':
    GPIO.output(4, GPIO.HIGH)

    responseBody = '''
    <html>
    <body>
        <h1>LED Turned ON!</h1>
        <br>
        <a href="../led_control.html">Back To Control Page!</a>
    </body>
    </html>
    '''

elif request.upper() == 'OFF':
    GPIO.output(4, GPIO.LOW)

    responseBody = '''
    <html>
    <body>
        <h1>LED Turned OFF!</h1>
        <br>
        <a href="../led_control.html">Back To Control Page!</a>
    </body>
    </html>
    '''

else:
    responseBody = '''
    <html>
    <body>
        <h1>Bad Command!</h1>
        <br>
        <a href="../led_control.html">Back To Control Page!</a>
    </body>
    </html>
    '''

print(responseBody)
