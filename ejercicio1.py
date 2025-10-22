import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

pin_led = 7

GPIO.setup(pin_led, GPIO.OUT)

for _ in range(4):
  GPIO.output(pin_led, GPIO.HIGH)
  sleep(1)
  GPIO.output(pin_led, GPIO.LOW)
  sleep(1)


GPIO.cleanup()