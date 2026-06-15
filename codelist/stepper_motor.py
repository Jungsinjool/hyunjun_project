import RPi.GPIO as GPIO
import time
in1 = 17
in2 = 18
in3 = 27
in4 = 22

step_sleep = 0.002
step_count = 4096
direction = True

step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
pins = [in1,in2,in3,in4]
step_counter = 0
def cleanup():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.cleanup()
try:
    i = 0
    for i in range(step_count):
        for pin in range(0, len(pins)):
            GPIO.output(pins[pin], step_sequence[step_counter][pin])
        if direction == True:
            step_counter = (step_counter - 1) % 8
        elif direction == False:
            step_counter = (step_counter + 1) % 8
        else:
            break
        time.sleep(step_sleep)
except KeyboardInterrupt:
    cleanup()
    exit(1)
cleanup()
exit(0)