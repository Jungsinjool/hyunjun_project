import RPi.GPIO as GPIO
import time

sr = 20
sensor = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(sr, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

GPIO.output(sr, GPIO.LOW)

def motion_callback(channel):
    GPIO.output(sr, GPIO.HIGH)
    print("Motion Detected !")
    time.sleep(2)
    
    for _ in range(3):
        GPIO.output(sr, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(sr, GPIO.LOW)
        time.sleep(0.1)
    
GPIO.add_event_detect(sensor, GPIO.RISING, callback=motion_callback, bouncetime=500)
print("PIR Monitering..")

try:
    
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("interrupted... ")

finally:    
    GPIO.cleanup()