import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

pin_led_r = 7
pin_led_n = 3
pin_led_v = 37

GPIO.setup(pin_led_r, GPIO.OUT)
GPIO.setup(pin_led_n, GPIO.OUT)
GPIO.setup(pin_led_v, GPIO.OUT)

GPIO.output(pin_led_r, GPIO.LOW)
GPIO.output(pin_led_n, GPIO.LOW)
GPIO.output(pin_led_v, GPIO.LOW)

for _ in range(4):

  GPIO.output(pin_led_r, GPIO.HIGH)
  sleep(1)
  GPIO.output(pin_led_r, GPIO.LOW)
  
  GPIO.output(pin_led_n, GPIO.HIGH)
  sleep(1)
  GPIO.output(pin_led_n, GPIO.LOW)  
  
  GPIO.output(pin_led_v, GPIO.HIGH)
  sleep(1)
  GPIO.output(pin_led_v, GPIO.LOW)


GPIO.cleanup()