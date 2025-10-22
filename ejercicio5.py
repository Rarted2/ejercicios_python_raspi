#Bueno los leds nos están dando juego suficiente, pero y si invitamos a otro elemento como es un
#botón pulsador y conseguimos encender dicho led cuando se pulse y se apague cuando no se esté
#pulsando.


    
    
import RPi.GPIO as GPIO
from time import sleep
##
GPIO.setmode(GPIO.BOARD)
##
pin_pul = 7
pin_led = 11
##
GPIO.setup(pin_pul, GPIO.IN, pull_up_down=GPIO.PUD_UP) #El pulsador, entrada
GPIO.setup(pin_led, GPIO.OUT)#Led, salida
##
try:
  while True:
    pulsado = GPIO.input(pin_pul)
    if pulsado == GPIO.LOW:
      GPIO.output(pin_led, True) #enciende el led
      #print('Pulsado')
    else:
    #pulsado == GPIO.UP:
      GPIO.output(pin_led, False) #apaga el led
  time.sleep(0.2)
except KeyboardInterrupt:
  GPIO.cleanup()
  print('/n' 'Finalizado manualmente')