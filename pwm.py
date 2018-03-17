import RPi.GPIO as GPIO
import time
pwmPin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin, GPIO.OUT)
p = GPIO.PWM(pwmPin,100 )
p.start(0)
#1/100 = 10ms
while True:
        for i in range(100):
                p.ChangeDutyCycle(i)
                time.sleep(0.01)
        for i in range(100):
                p.ChangeDutyCycle(100-i)
                time.sleep(0.01)
