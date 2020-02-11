#Object Detection using IR sensor
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
GPIO.setup(27,GPIO.IN)
#setting object as mylcd and initialization
mylcd=lcd.lcd()
mylcd.begin(D4,D5,D6,D7,RS,EN)
mylcd.clear()
count = 0
val = 0
if __name__=="__main__":
    try:
        while True:
            mylcd.clear()
            value=GPIO.input(27)
            if value==1:        
                time.sleep(1)
                val = GPIO.input(27)
                if val == 0:
                    count +=1
                mylcd.Print("Object Detected")
                mylcd.setCursor(2,1)
                mylcd.Print("VisitorNo:"+str(count))
                time.sleep(1)
                
    except KeyboardInterrupt:
        GPIO.cleanup()