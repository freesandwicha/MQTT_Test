# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 21/8/2023 5:42 pm

import paho.mqtt.client as mqtt
import time
# we create two mqtt publishers(clients) faking the inside temperature from a heating device
# and one faking the outside temperature from an outside temperature sensor
# and then we are writing a receiver or a subscriber to subscribe


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))
#Connect the broker and create a client:
mqttBroker = "mqtt.eclipseprojects.io"
# The public test MQTT broker service.
client = mqtt.Client("Smart phone")
client.connect(mqttBroker)

#Subscribe the topic from  Clients

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message

time.sleep(30)
client.loop_stop()
