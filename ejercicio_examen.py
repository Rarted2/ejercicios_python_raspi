import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

pin_pwm1 = 12
pin_pwm2 = 11

GPIO.setup(pin_pwm1, GPIO.OUT)  #Configura el PWM como salida
GPIO.setup(pin_pwm2, GPIO.OUT)  #Configura el PWM como salida

#Inicializar PWM1 con 1000 Hz y empezar con duty cycle 0
pwm1 = GPIO.PWM(pin_pwm1, 1000)
pwm1.start(0)
#Inicializar PWM2 con 1000 Hz y empezar con duty cycle 0
pwm2 = GPIO.PWM(pin_pwm2, 1000)
pwm2.start(0)

try:    #Para cuando hay un error, se vuelve a ejecutar el codigo
    for duty_cycle in range(0, 101, 5):
            pwm1.ChangeDutyCycle(duty_cycle)
            sleep(0.1)
            
            
    for _ in range(4):
        for duty_cycle in range(0, 101, 5): 
            pwm1.ChangeDutyCycle(100 - duty_cycle)
            pwm2.ChangeDutyCycle(duty_cycle)
            sleep(0.1)
            
            
        for duty_cycle in range(0, 101, 5):
            pwm1.ChangeDutyCycle(duty_cycle)
            pwm2.ChangeDutyCycle(100 - duty_cycle)
            sleep(0.1)
            
    for duty_cycle in range(0, 101, 5): 
            pwm1.ChangeDutyCycle(100 - duty_cycle)
            pwm2.ChangeDutyCycle(duty_cycle)
            sleep(0.1)
            
            
except KeyboardInterrupt:
    print("Programa terminado")

finally:
    # Detener PWM y limpiar GPIO
    print("Deteniendo PWM y limpiando pines...")
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()