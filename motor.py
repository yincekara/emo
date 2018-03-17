import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pwmPin = 35
GPIO.setup(pwmPin, GPIO.OUT)
p = GPIO.PWM(pwmPin,50)
p.start(7.5) #0 C
while True:
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
    p.ChangeDutyCycle(5)
    time.sleep(1)
    p.ChangeDutyCycle(10)
    time.sleep(1)
    #(2/20) * 100 10  90 C
    #(1/20) * 100 5   -90 C
