#Program To Demonstrate UltraSonic Sensor
import RPi.GPIO as GPIO
import time
import lcd

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 19
GPIO_ECHO = 20

D4=12
D5=13
D6=16
D7=17
RS=5
EN=6

GPIO.cleanup()

#setting object as mylcd and initialization
mylcd=lcd.lcd()
mylcd.begin(D4,D5,D6,D7,RS,EN)
mylcd.clear()
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.setup(23,GPIO.OUT)

def distance():
    GPIO.output(GPIO_TRIGGER,True)
    
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(GPIO_ECHO)==0:
        StartTime = time.time()
        
    while GPIO.input(GPIO_ECHO)==1:
        StopTime = time.time()
        
    TimeElapsed = StopTime-StartTime
    
    dist = (TimeElapsed*34300)/2
    
    return dist


if __name__ == '__main__':
    try:
        while True:
            mylcd.clear()
            dist = distance()
            print("Distance : %.1f cm" % dist)
            
            mylcd.Print("Distance : %.1f CM" % dist) 
            time.sleep(1)
            
            
            if dist <= 10:
                GPIO.output(23,GPIO.HIGH)
                mylcd.setCursor(2,1)
                mylcd.Print("Overflow")
            else:
                GPIO.output(23,GPIO.LOW)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Mesaurement Stopped by User")        
        GPIO.cleanup()        

    