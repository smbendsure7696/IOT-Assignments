#Program To Glow LEDs
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

def alternate():
    GPIO.output(16,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(16,GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.2)
    
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    time.sleep(0.2)
def destroy():
    GPIO.cleanup()

if __name__=='__main__':
    try:
        while True:
            value = 0#GPIO.input(20)
            value2 = GPIO.input(21)
            if value==0:
                alternate()
    except KeyboardInterrupt:
        destroy()