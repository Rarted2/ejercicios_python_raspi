import RPi.GPIO as GPIO
from time import sleep

try:
    
    led_amarillo = 13
    led_rojo = 11
    led_verde = 7
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_verde,GPIO.OUT)
    GPIO.setup(led_rojo,GPIO.OUT)
    GPIO.setup(led_amarillo,GPIO.OUT)
    
    GPIO.output(led_verde,GPIO.HIGH)
    sleep(2)
    GPIO.output(led_verde,GPIO.LOW)
    
    GPIO.output(led_rojo,GPIO.HIGH)
    sleep(2)
    GPIO.output(led_rojo,GPIO.LOW)
    
    
    GPIO.output(led_amarillo,GPIO.HIGH)
    sleep(2)
    GPIO.output(led_amarillo,GPIO.LOW)
    
    
except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
