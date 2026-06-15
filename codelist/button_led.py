import RPi.GPIO as GPIO
import time

button_pin = 15
led_pin = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
    if GPIO.input(button_pin) == GPIO.HIGH:
        GPIO.output(led_pin, 1)
    else:
        GPIO.output(led_pin, 0)
    time.sleep(0.1)    