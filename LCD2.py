import lcd #import lcd library in the same folder
import time #import time for sleep function
import RPi.GPIO as GPIO #to use gpio on raspberry pi

#setting pins and do the same gpio connections
D4=12
D5=13
D6=16
D7=17
RS=5
EN=6

#cleanup
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
#setting object as mylcd and initialization
mylcd=lcd.lcd()
mylcd.begin(D4,D5,D6,D7,RS,EN)
mylcd.clear()
if __name__ == '__main__':
    try:
        while True:
            mylcd.clear()
            time.sleep(1)
            mylcd.Print("Be Kind")
            mylcd.shift(mylcd.right,5)
            mylcd.shift(mylcd.left,5)
            time.sleep(1)
            
    except KeyboardInterrupt:
        GPIO.cleanup()