from gpiozero import LED
import time

led = LED(4)

for i in range(10):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
 
