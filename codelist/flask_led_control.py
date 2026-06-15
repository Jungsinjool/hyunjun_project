#!/usr/#!/usr/bin/python3

from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 4

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('led_control.html')


@app.route('/flask_led', methods=['GET', 'POST'])
def led_control():

    control = None

    if request.method == 'GET':
        control = request.args.get('action')

    elif request.method == 'POST':
        control = request.form.get('action')

    if control == 'on':
        GPIO.output(LED, GPIO.HIGH)

    elif control == 'off':
        GPIOtput(LED, GPIO.LOW)

    else:
        return "<h1>Bad Command!</h1>"

    return render_template('result.html', status=control)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)bin/python3

from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 4

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('led_control.html')


@app.route('/flask_led', methods=['GET', 'POST'])
def led_control():

    control = None

    if request.method == 'GET':
        control = request.args.get('action')

    elif request.method == 'POST':
        control = request.form.get('action')

    if control == 'on':
        GPIO.output(LED, GPIO.HIGH)

    elif control == 'off':
        GPIOtput(LED, GPIO.LOW)

    else:
        return "<h1>Bad Command!</h1>"

    return render_template('result.html', status=control)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
