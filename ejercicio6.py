import time

import RPi.GPIO as GPIO

# Pin de control del LED (PWM)
LED_PIN = 12  # Pin 12 (GPIO18 en modo BCM)

# Frecuencia PWM
PWM_FREQUENCY = 1000  # Hz

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
print(f"Configurando PWM en el pin {LED_PIN} con frecuencia {PWM_FREQUENCY} Hz.")

p = GPIO.PWM(LED_PIN, PWM_FREQUENCY)
p.start(0)  # Empezar con un ciclo de trabajo del 0%

try:
    print("Encendiendo el LED progresivamente...")
    for dc in range(0, 101, 1):  # Aumentar el ciclo de trabajo de 0 a 100
        p.ChangeDutyCycle(dc)
        time.sleep(0.01)  # Pequeña pausa para ver el efecto
    print("LED encendido al 100%.")
    time.sleep(2) # Mantener encendido por un tiempo
    print("Apagando el LED progresivamente...")
    for dc in range(100, -1, -1): # Disminuir el ciclo de trabajo de 100 a 0
        p.ChangeDutyCycle(dc)
        time.sleep(0.01)
    print("LED apagado.")

except KeyboardInterrupt:
    print("Interrupción por teclado. Apagando...")
finally:
    p.stop()  # Detener el PWM
    GPIO.cleanup() # Limpiar los pines GPIO