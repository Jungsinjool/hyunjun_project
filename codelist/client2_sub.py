import paho.mqtt.client as mqtt

broker = "localhost"
topic = "temperature"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code",rc)
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"[RECIVED] {msg.payload.decode()} C")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)

client.loop_forever()
