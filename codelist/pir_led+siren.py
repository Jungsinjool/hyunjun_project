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

GPIO.output(led_yellow, GPIO.HIGH)
GPIO.output(led_red, GPIO.LOW)

def motion_callback(channel):
    GPIO.output(led_yellow, GPIO.LOW)
    GPIO.output(led_red, GPIO.HIGH)
    print("Motion Detected !")
    time.sleep(2)
    
    GPIO.output(led_yellow, GPIO.HIGH)
    GPIO.output(led_red, GPIO.LOW)
GPIO.add_event_detect(sensor, GPIO.RISING, callback=motion_callback, bouncetime=300)
print("PIR Monitering..")

try:
    
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("interrupted... ")

finally:    
    GPIO.cleanup()