# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 21/8/2023 5:23 pm

import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
# we create two mqtt publishers(clients) faking the inside temperature from a heating device
# and one faking the outside temperature from an outside temperature sensor
# and then we are writing a receiver or a subscriber to subscribe


#Connect the broker and create a client:
mqttBroker = "mqtt.eclipseprojects.io"
# The public test MQTT broker service.
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

#Publish the topic from Client to the Broker
while True:
    randNumber = uniform(20.0, 21.0)
    #Get a float number between 20.0 and 21.0
    client.publish("TEMPERATURE", randNumber)
    #The topic is named TEMPERATURE,  and the content is a random number.
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)


