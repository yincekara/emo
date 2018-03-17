import RPi.GPIO as GPIO
import time
while True:
        GPIO.setmode(GPIO.BOARD)

        TRIG=35
        ECHO=37
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)


        GPIO.output(TRIG,False)
        time.sleep(1)
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)
        timeStart = time.time()

        while GPIO.input(ECHO)==0:
                timeStart = time.time()
        while GPIO.input(ECHO)==1:
                timeStop = time.time()
        totalTime = (timeStop - timeStart) / 2
        distance = totalTime * 34300
        print("Mesafe ", distance)
        GPIO.cleanup()
