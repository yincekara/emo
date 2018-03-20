import RPi.GPIO as GPIO
import dht11
import time
import datetime
import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("192.168.4.142", 1883, 60)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()



instance = dht11.DHT11(pin=14)
while True:
    result = instance.read()
    if result.is_valid():
    print("Temperature: %d C" % result.temperature)
    client.publish("deneme/",str(result.temperature))
    time.sleep(5)
