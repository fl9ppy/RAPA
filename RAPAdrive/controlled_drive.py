from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# Setup GPIO pins for motor control
GPIO.setmode(GPIO.BCM)
left_motor_pin1 = 17
left_motor_pin2 = 18
right_motor_pin1 = 22
right_motor_pin2 = 23
GPIO.setup(left_motor_pin1, GPIO.OUT)
GPIO.setup(left_motor_pin2, GPIO.OUT)
GPIO.setup(right_motor_pin1, GPIO.OUT)
GPIO.setup(right_motor_pin2, GPIO.OUT)

# Function to control left motor
def control_left_motor(direction):
    if direction == 'forward':
        GPIO.output(left_motor_pin1, GPIO.HIGH)
        GPIO.output(left_motor_pin2, GPIO.LOW)
    elif direction == 'backward':
        GPIO.output(left_motor_pin1, GPIO.LOW)
        GPIO.output(left_motor_pin2, GPIO.HIGH)
    else:
        GPIO.output(left_motor_pin1, GPIO.LOW)
        GPIO.output(left_motor_pin2, GPIO.LOW)

# Function to control right motor
def control_right_motor(direction):
    if direction == 'forward':
        GPIO.output(right_motor_pin1, GPIO.HIGH)
        GPIO.output(right_motor_pin2, GPIO.LOW)
    elif direction == 'backward':
        GPIO.output(right_motor_pin1, GPIO.LOW)
        GPIO.output(right_motor_pin2, GPIO.HIGH)
    else:
        GPIO.output(right_motor_pin1, GPIO.LOW)
        GPIO.output(right_motor_pin2, GPIO.LOW)

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Control route
@app.route('/control', methods=['POST'])
def control():
    direction = request.form['direction']
    if direction == 'forward' or direction == 'backward':
        control_left_motor(direction)
        control_right_motor(direction)
    elif direction == 'left':
        control_left_motor('backward')
        control_right_motor('forward')
    elif direction == 'right':
        control_left_motor('forward')
        control_right_motor('backward')
    else:
        control_left_motor('stop')
        control_right_motor('stop')
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
