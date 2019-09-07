
import RPi.GPIO as GPIO
from time import sleep

class Robot:
    """
    Robot class
    """
    def __init__(self, name):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(13, GPIO.OUT) # Left
        GPIO.setup(15, GPIO.OUT) # Left
        GPIO.setup(16, GPIO.OUT) # Right
        GPIO.setup(18, GPIO.OUT) # Right
    
    def forward(self, x):
        print('forward')
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        sleep(x)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)

    def backward(self, x):
        print('backward')
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        sleep(x)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
    
    
    def right(self, x):
        print('right')
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        sleep(x)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
    
    def left(self, x):
        print('left')
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        sleep(x)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
    
    def delete(self):
        GPIO.cleanup()
