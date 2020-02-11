#Program to Write data on ThingsSpeak
import spidev
import time
import urllib2

spi = spidev.SpiDev()
spi.open(0,0)
myApi = 'YourApiKeyHere'
baseUrl = 'https://api.thingspeak.com/update?api_key=%s' % myApi

def readadc(adcnum):
    if adcnum>7 or adcnum<0:
        return -1
    r = spi.xfer2([1,8+adcnum<<4,0])
    adcout = ((r[1]&3)<<8)+r[2] 
    return adcout

while True:
    value = readadc(0)
    volts = (value*3.3)/1024
    temperature = volts/(100.0/1000)
    con = urllib2.urlopen(baseUrl+'&field1=%s' %(temperature))
    print("%4d/1023 => %5.3f => %4.1f A `C" % (value,volts,temperature))
    print con.read()
    con.close()
    time.sleep(10)