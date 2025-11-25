import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)

verde_led = 12             

GPIO.setup(verde_led, GPIO.OUT)


pwm_led = GPIO.PWM(verde_led, 1000)
pwm_led.start(0)        


for duty_cycle in range(0, 100, 1): 
            pwm_led.ChangeDutyCycle(duty_cycle)
            sleep(0.1)
sleep(1)
pwm_led.stop()
GPIO.cleanup()