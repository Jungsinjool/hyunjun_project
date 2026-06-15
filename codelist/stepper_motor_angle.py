import RPi.GPIO as GPIO
import time
in1 = 17
in2 = 18
in3 = 27
in4 = 22

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

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
pins = [in1,in2,in3,in4]

step_counter = 0

current_position = 0
step_per_degree = 4096 / 360

def move_steps(steps, direction):
    global step_counter
    for _ in range(abs(int(steps))):
        for pin in range(4):
            GPIO.output(pins[pin], step_sequence[step_counter][pin])
            
        if direction:
            step_counter =(step_counter + 1) % 4
        else:
            step_counter =(step_counter - 1) % 4
            
        time.sleep(step_sleep)

def move_to(angle):
    global current_position
    
    diff = angle - current_position
    steps = diff * step_per_degree
    
    if diff>0:
        move_steps(steps, True)
    else:
        move_steps(steps, False)
    
    current_position = angle

try:
    while True:
        target = int(input("각도 입력 (0~180):"))
        move_to(target)

except KeyboardInterrupt:
    GPIO.cleanup()