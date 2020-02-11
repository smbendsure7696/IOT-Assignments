#RAS[BERRY PI BASED PROGRAM TO MEASURE TEMPERATURE AND HUMIDITY USING DHT11

#we need to import the libraries
import time #to use sleep function
import RPi.GPIO as GPIO # GPIO object from the RPi.GPIO library
import urllib2
import thingspeak
channelId = 982119

myApi = 'Write Your ApiKey Here'

channel = thingspeak.Channel(id = channelId,api_key = myApi)
#read = channel.get_last_data_age(field="field1")
read = channel.get_field('field1')
read1 = channel.get_field('field2')
print read
print
print read1

for fields in read:
    print fields

