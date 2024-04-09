import time

class GPIO:
    BCM = 'BCM'
    OUT = 'OUT'
    HIGH = 'HIGH'
    LOW = 'LOW'
    
    #@staticmethod
    def setmode(mode):
        print("Setting GPIO mode to", mode)
        
    #@staticmethod
    def setup(pin, direction):
        print("Setting up pin", pin, "as", direction)
        
    #@staticmethod
    def output(pin,value):
        print("Setting output of pin", pin, "to", value)
        
#pini pt motor control
LEFT_FORWARD_PIN = 17
LEFT_BACKWARD_PIN = 18
RIGHT_FORWARD_PIN = 22
RIGHT_BACKWARD_PIN = 23
    
    #clasa pt motor controller
class MotorController:
    def __innit__(self):
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(LEFT_FORWARD_PIN, GPIO.OUT)
         GPIO.setup(LEFT_BACKWARD_PIN, GPIO.OUT)
         GPIO.setup(RIGHT_FORWARD_PIN, GPIO.OUT)
         GPIO.setup(RIGHT_BACKWARD_PIN, GPIO.OUT)
         
    def move_forward(self):
        GPIO.output(LEFT_FORWARD_PIN, GPIO.HIGH)
        GPIO.output(RIGHT_FORWARD_PIN, GPIO.HIGH)

    def move_backward(self):
        GPIO.output(LEFT_BACKWARD_PIN, GPIO.HIGH)
        GPIO.output(RIGHT_BACKWARD_PIN, GPIO.HIGH)

    def turn_left(self):
        GPIO.output(RIGHT_FORWARD_PIN, GPIO.HIGH)

    def turn_right(self):
        GPIO.output(LEFT_FORWARD_PIN, GPIO.HIGH)

    def stop(self):
        GPIO.output(LEFT_FORWARD_PIN, GPIO.LOW)
        GPIO.output(LEFT_BACKWARD_PIN, GPIO.LOW)
        GPIO.output(RIGHT_FORWARD_PIN, GPIO.LOW)
        GPIO.output(RIGHT_BACKWARD_PIN, GPIO.LOW)
             
def main():
    try:
        motor_controller = MotorController()
        
        #testare miscari
        print("Moving forward...")
        motor_controller.move_forward()
        time.sleep(2)
        
                print("Moving backward...")
        motor_controller.move_backward()
        time.sleep(2)

        print("Turning left...")
        motor_controller.turn_left()
        time.sleep(1)

        print("Turning right...")
        motor_controller.turn_right()
        time.sleep(1)

    except KeyboardInterrupt:
        print("Stopping the robot...")
    finally:
        # Cleanup GPIO (simulated)
        print("Cleaning up GPIO")
        motor_controller.stop()

if __name__ == "__main__":
    main()

