import paho.mqtt.client as mqtt
import board
import busio
import adafruit_bmp280
import time

broker = "203.250.133.87"

client = mqtt.Client()
client.connect(broker, 1883, 60)

i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c,address=0x76)


while True:
    temp = round(bmp280.temperature, 1)

    client.publish(
            "home/temperature",
            str(temp)
        )
    print("temperature: ", temp)

    time.sleep(5)
