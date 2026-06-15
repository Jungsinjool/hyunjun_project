from gpiozero import Button
from picamera2 import Picamera2, Preview
from time import sleep
#create button objects
button1 = Button(2)# GPIO2, pullup
button2 = Button(3)# GPIO3, pullup
#create picamera2 object
camera = Picamera2()
camera_config = camera.create_preview_configuration()
camera.configure(camera_config)
#start the camera
camera.start_preview(Preview.QTGL)
camera.start()
quit_flag = False
i = 0
#stop the camera when the button2 is pressed
def stop_camera():
    global quit_flag
    camera.stop_preview()
    camera.stop()
    quit_flag = True
    print('stop the camera and exit')
#capture a still image when button1 is pressed
def capture_image():
    global i
    i = i + 1
    camera.capture_file('image_{}.jpg'.format(i))
    print('still image has been taken')
    sleep(3)
#assign a function that runs when the buttons are pressed
button1.when_pressed = capture_image
button2.when_pressed = stop_camera
while True:
    if quit_flag == False:
        sleep(1)
    else:
        exit(0)