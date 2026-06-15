#!/usr/bin/python3
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO


LED_PIN = 4

def on_connect(client, userdata, flags, rc):
    print("Connected with RC: " + str(rc))
    client.subscribe("home/led", 0)

def on_message(client, userdata, msg):
    #print ("Topic: "+ msg.topic+" \nMessage: "str(msg.payload))
    command = msg.payload.decode()
    if command == "on":
        print("LED on")
        GPIO.output(4, True)
    elif command == "off":
        print("LED off")
        GPIO.output(4, False)
    else:
        print("Unknown Command")


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message

client.connect("203.250.133.87", 1883, 60)


try:
    client.loop_forever()
except KeyboardInterrupt:
    print("terminated")

finally:
    GPIO.cleanup()

