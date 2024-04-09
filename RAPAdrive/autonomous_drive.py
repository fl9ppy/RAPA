import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG_LEFT = 23
ECHO_LEFT = 24
TRIG_RIGHT = 17
ECHO_RIGHT = 27

GPIO.setup(TRIG_LEFT, GPIO.OUT)
GPIO.setup(ECHO_LEFT, GPIO.IN)
GPIO.setup(TRIG_RIGHT, GPIO.OUT)
GPIO.setup(ECHO_RIGHT, GPIO.IN)

def measure_distance(trigger_pin, echo_pin):
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()
    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

try:
    while True:
        distance_left = measure_distance(TRIG_LEFT, ECHO_LEFT)
        distance_right = measure_distance(TRIG_RIGHT, ECHO_RIGHT)

        if distance_left < distance_right:
            print("Turning left")
        else:
            print("Turning right")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
