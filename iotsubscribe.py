import paho.mqtt.client as mqtt
import os
def on_connect(client, userdata, flags, rc):
print("Connected with result code "+str(rc))
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
#client.subscribe("$SYS/#")
client.subscribe("command/")


def on_message(client, userdata, msg):
#print(msg.topic+" "+str(msg.payload))
print("command executed: " + msg.payload)
os.system(msg.payload)



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.4.142", 1883, 60)
client.loop_forever()
