#write program to controlling a relay
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(21,GPIO.IN,pull_up_down = GPIO.PUD_UP)
prev = GPIO.input(21)

try:
    while True:
        value = GPIO.input(21)
        while value==0:
            val = GPIO.input(21)
            if val == 0:
                GPIO.output(26,GPIO.LOW)
                break
            GPIO.output(26,GPIO.HIGH)
        #if value==prev:
         #       GPIO.output(26,GPIO.LOW)     
                
except KeyboardInterrupt:
    GPIO.cleanup()