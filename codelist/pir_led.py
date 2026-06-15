import RPi.GPIO as GPIO
import time

led_red = 20
led_yellow= 21
sensor = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

time.sleep(5)
try:
    
    while True:
    
        if GPIO.input(sensor) == 1:
            GPIO.output(led_yellow, 0)
            GPIO.output(led_red, 1)
            print("Motion Detected !")
            time.sleep(2)
        else:
            GPIO.output(led_yellow, 1)
            GPIO.output(led_red, 0)
            time.sleep(1)

except KeyboardInterrupt:
    print("interrupted... ")
    GPIO.cleanup()