import RPi.GPIO as GPIO
import time

buton=35
led=37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buton,GPIO.IN,pull_up_down = GPIO.PUD_UP)
while True:
        button_state= GPIO.input(buton)
        if (button_state==False):
                GPIO.output(led,GPIO.HIGH)
                print("butona basildi")
                #bouncing
                time.sleep(0.2)
        else:
                GPIO.output(led,GPIO.LOW)
                #print("buton birakildi")
