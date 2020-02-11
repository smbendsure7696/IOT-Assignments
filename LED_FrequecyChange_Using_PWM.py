#Program to Change Frequency of LED
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)

LED = GPIO.PWM(26,100)
LED.start(0)

while True:
    for x in range(50):
        LED.ChangeDutyCycle(x)
        time.sleep(0.1)
        
    for x in range(50):
        LED.ChangeDutyCycle(50-x)
        time.sleep(0.1)    