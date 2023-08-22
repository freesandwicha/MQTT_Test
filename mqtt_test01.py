# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 22/8/2023 8:23 pm

import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST")
MQTT_PORT = int(os.getenv("MQTT_PORT", 8883))
MQTT_PROTOCOL = os.getenv("MQTT_PROTOCOL")
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")


# Callback when client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker successfully!")
    else:
        print(f"Failed to connect with error code: {rc}")

    # Subscribing to the topic user provided (this is done within on_connect so that we resubscribe upon reconnection)
    client.subscribe(topic)


# Callback when a message is received from the server.
def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}' with QoS {msg.qos}")


# Callback to confirm the delivery of the payload.
def on_publish(client, userdata, mid):
    print(f"Payload successfully published to topic '{topic}' with message ID: {mid}")


# User input for topic and payload
topic = input("Enter the topic you wish to publish to: ")
payload = input("Enter the payload you wish to send: ")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

# Setting up username and password if provided in the environment variables
if MQTT_USERNAME and MQTT_PASSWORD:
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

client.connect(MQTT_HOST, MQTT_PORT)

# Begin the network loop
client.loop_start()

# Publish the payload
client.publish(topic, payload)

try:
    # Continue the loop indefinitely to keep the connection alive
    while True:
        pass
except KeyboardInterrupt:
    # Stop the loop and disconnect when user wants to exit
    client.loop_stop()
    client.disconnect()
