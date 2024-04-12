import RPi.GPIO as GPIO
import time

# GPIO pins for the servos
SERVO_UP_DOWN_PIN = 18
SERVO_RIGHT_LEFT_PIN = 19

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_UP_DOWN_PIN, GPIO.OUT)
GPIO.setup(SERVO_RIGHT_LEFT_PIN, GPIO.OUT)

# Set up PWM for servos
pwm_up_down = GPIO.PWM(SERVO_UP_DOWN_PIN, 50)  # 50 Hz frequency
pwm_right_left = GPIO.PWM(SERVO_RIGHT_LEFT_PIN, 50)

# Start PWM with initial duty cycles (neutral position)
pwm_up_down.start(7.5)  # 7.5% duty cycle for neutral position
pwm_right_left.start(7.5)

def move_servos_up_down(angle):
    duty_cycle = angle / 18 + 2  # Convert angle to duty cycle
    pwm_up_down.ChangeDutyCycle(duty_cycle)

def move_servos_right_left(angle):
    duty_cycle = angle / 18 + 2  # Convert angle to duty cycle
    pwm_right_left.ChangeDutyCycle(duty_cycle)

try:
    while True:
        # Get user input for servo positions
        up_down_angle = float(input("Enter up-down angle (0 to 180): "))
        right_left_angle = float(input("Enter right-left angle (0 to 180): "))

        # Move servos to specified positions
        move_servos_up_down(up_down_angle)
        move_servos_right_left(right_left_angle)

except KeyboardInterrupt:
    # Clean up GPIO
    pwm_up_down.stop()
    pwm_right_left.stop()
    GPIO.cleanup()
