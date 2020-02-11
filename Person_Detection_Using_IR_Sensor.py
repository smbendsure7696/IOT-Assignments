#Person is there in room switch on LED if person goes out switch out LED
#import lcd #import lcd library in the same folder
import time #import time for sleep function
import RPi.GPIO as GPIO #to use gpio on raspberry pi

#cleanup
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(25,GPIO.IN,pull_up_down = GPIO.PUD_UP)
count = 0
ocount = 0
val = 0

if __name__=="__main__":
    try:
        while True:
            SW1value = GPIO.input(24)
            SW2value = GPIO.input(25)
            if SW1value==0 and SW2value==1:
                s1 = GPIO.input(24)
                s2 = GPIO.input(25)
                if s2 == 0 and s1 == 1:
                    count +=1
                    GPIO.output(22,GPIO.HIGH)
                    print("In Count: ",count)    
            if SW2value==0 and SW1value==1:
                s1 = GPIO.input(24)
                s2 = GPIO.input(25)
                if s1 == 0 and s2 == 1:
                    ocount +=1
                    GPIO.output(22,GPIO.LOW)
                    print("Out Count: ",ocount)
    except KeyboardInterrupt:
        GPIO.cleanup()
