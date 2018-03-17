import  RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pin=29
GPIO.setup(pin,GPIO.OUT)
while True:
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)
