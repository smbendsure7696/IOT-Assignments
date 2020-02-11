#write program to detect motion using motion Sensors
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
try:
    while True:
        value = GPIO.input(24)
        if value==1:
            GPIO.output(5,GPIO.HIGH)
            GPIO.output(6,GPIO.HIGH)
            GPIO.output(12,GPIO.HIGH)
            GPIO.output(13,GPIO.HIGH)
            GPIO.output(16,GPIO.HIGH)
            GPIO.output(17,GPIO.HIGH)
            GPIO.output(18,GPIO.HIGH)
            print("Motion Detected")
        else:
            GPIO.output(5,GPIO.LOW)
            GPIO.output(6,GPIO.LOW)
            GPIO.output(12,GPIO.LOW)
            GPIO.output(13,GPIO.LOW)
            GPIO.output(16,GPIO.LOW)
            GPIO.output(17,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)
        
except KeyboardInterrupt:
    GPIO.cleanup()