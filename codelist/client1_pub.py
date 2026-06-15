import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"
topic = "temperature"

client = mqtt.Client()
client.connect(broker,1883, 60)

while True:
    temp = round(random.uniform(20.0, 35.0),)
    message = str(temp)

    client.publish(topic, message)
    print(f"[publish] Temperature: {message}")

    time.sleep(2)
