

import os
import paho.mqtt.client as mqtt
#The main function of this script is to connect to the MQTT server,
# get the subject and message entered by the user,
# and post the message to that subject.
# It also subscribes to that topic to receive an acknowledgement and ends when an acknowledgement is received.


# Get MQTT credentials from env variables or  defaults
MQTT_HOST = os.environ.get('MQTT_HOST', 'localhost')
MQTT_PORT = 8883
MQTT_USERNAME = os.environ.get('MQTT_USERNAME', '')
MQTT_PASSWORD = os.environ.get('MQTT_PASSWORD', '')

received_confirmation: bool = False

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker successfully!")
    else:
        print(f"Failed to connect with error code: {rc}")
    topic = input("Please enter the topic you wish to publish to: ")
    message = input("Please enter the message payload you wish to send: ")
    client.subscribe(topic)  # Subscribe to topics entered by the user to receive confirmations
    client.publish(topic, message)
    print(f"\nPublished to {topic}:")
    print(f"{message}")


def on_message(client, userdata, msg):
    global received_confirmation
    print(f"Received confirmation for message '{msg.payload.decode()}' on topic '{msg.topic}'")
    received_confirmation = True
    #It indicates that the MQTT server has received the published message.

client = mqtt.Client() #Create a client object
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)  # Set the username and password.
client.on_connect = on_connect # When we successfully connect to the MQTT server, execute this specific on_connect function.
client.on_message = on_message # When we successfully receive new message from the MQTT server, execute this sepcific on_message function.

client.connect(MQTT_HOST, MQTT_PORT, 60)

try:
    client.loop_start()
    while not received_confirmation:
        pass  # Keep this script running until get confirmation.
finally:
    client.loop_stop()  #  Stop loop
    client.disconnect()  #  disconnect