import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

pin_led_rojo = 7

pin_led_naranja = 3

GPIO.setup(pin_led_rojo, GPIO.OUT)
GPIO.setup(pin_led_naranja, GPIO.OUT)


GPIO.output(pin_led_rojo, GPIO.LOW)
GPIO.output(pin_led_naranja, GPIO.LOW)

for _ in range(4):

  
  GPIO.output(pin_led_rojo, GPIO.HIGH)
  GPIO.output(pin_led_naranja, GPIO.LOW)
  sleep(1)
  GPIO.output(pin_led_rojo, GPIO.LOW)
  GPIO.output(pin_led_naranja, GPIO.HIGH)
  sleep(1)


GPIO.cleanup()