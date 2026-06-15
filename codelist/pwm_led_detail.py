import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
p = GPIO.PWM(4, 100)
p.start(50)

try:
    while 1:
        for freq in range(1, 500, 10):
            p.ChangeFrequency(freq)
            time.sleep(0.1)
        time.sleep(0.1)    
        for freq in range(500, 1, -10):
            p.ChangeFrequency(freq)
            time.sleep(0.1)
        
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()