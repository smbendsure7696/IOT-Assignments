#Program To Demonstrate LCD
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

if __name__ == '__main__':
    while True:
        try:
            mylcd.clear()
            time.sleep(1)
            mylcd.Print("FergussonCollege") 
            time.sleep(1)
            mylcd.setCursor(2,1)
            mylcd.Print("PUNE")
            time.sleep(1)
            
            mylcd.clear()
            mylcd.Print("M.Sc.C.A")
            mylcd.setCursor(2,9)
            mylcd.shift(mylcd.right,8)
            mylcd.shift(mylcd.left,8)
            
            mylcd.blinkCursorOn()
            time.sleep(2)
            mylcd.blinkCursorOff()
            mylcd.clear()
            time.sleep(2)
            
        except KeyboardInterrupt:
                #clean up of GPIOs
            GPIO.cleanup()
    
