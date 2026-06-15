import RPi.GPIO as GPIO
import time
in1 = 17
in2 = 18
in3 = 27
in4 = 22
button = 23

step_sleep = 0.003



step_sequence = [
    [1,0,0,1],
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
                ]
                 

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
pins = [in1,in2,in3,in4]
step_counter = 0

try:
    while True:
        if GPIO.input(button) == 0:
            for pin in range(4):
                GPIO.output(pins[pin], step_sequence[step_counter][pin])
                
            step_counter = (step_counter + 1) % 4
            time.sleep(step_sleep)
        else:
            time.sleep(0.01)
            
except KeyboardInterrupt:
    GPIO.cleanup()