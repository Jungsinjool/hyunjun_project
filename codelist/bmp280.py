
import time
from bmp280 import BMP280
from smbus2 import SMBus
print("press ctrl-c to stop!")
bus = SMBus(1)

bmp280 = BMP280(i2c_dev=bus)
while True:
    try:
        temperature = bmp280.get_temperature()
        pressure = bmp280.get_pressure()
        print('Temperature = {:.2f}C'.format(temperature))
        print('Pressure = {:.1f}hPa'.format(pressure))
        print("=======================")
        time.sleep(3)
    except KeyboardInterrupt:
        exit(0)