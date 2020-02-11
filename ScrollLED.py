#Program to Scroll LED
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
GPIO.setup(20,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(21,GPIO.IN,pull_up_down = GPIO.PUD_UP)
def blink(led):
    GPIO.output(led,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(led,GPIO.LOW)
    time.sleep(0.1)
    
def destroy():
    GPIO.cleanup()

if __name__=='__main__':
    try:
        while True:
            value = GPIO.input(20)
            value2 = GPIO.input(21)
            if value==0:
                blink(5)
                blink(6)
                blink(12)
                blink(13)
                blink(16)
                blink(17)
                blink(18)
                blink(19)
            if value2==0:
                blink(19)
                blink(18)
                blink(17)
                blink(16)
                blink(13)
                blink(12)
                blink(6)
                blink(5)
    except KeyboardInterrupt:
        destroy()