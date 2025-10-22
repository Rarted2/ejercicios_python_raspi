# Lo mismo que puede suceder en una casa, podría gustarnos tener la posibilidad de que el
# encendido de luz (en nuestro caso el led) se hiciera de una forma progresiva y no de golpe. Para ello
# hay que recurrir a la característica PWN de la Raspberry. Estableceremos para un funcionamiento
# adecuado una frecuencia de 1000 Hz aunque puedes probar con otras frecuencias a ver qué pasa.
# (¡Ojo con el pin que se utiliza ahora!)
# Material necesario: raspberry, protoboard, led rojo, resistencia pequeña, 2 cables macho-hembra


import RPi.GPIO as GPIO
from time import sleep

# --- Configuración Inicial ---
GPIO.setmode(GPIO.BOARD)

PIN_LED_PWM = 12 # Salida PWM para el LED (GPIO 18 BCM)

FRECUENCIA_PWM = 1000 # Frecuencia en Hertz (Hz)
INCREMENTO = 5        # Incremento en el ciclo de trabajo (Duty Cycle)
TIEMPO_PASO = 0.02    # Pausa entre incrementos (controla la velocidad de cambio)

# --- Setup de Pin ---
GPIO.setup(PIN_LED_PWM, GPIO.OUT)

# Inicializar PWM: Crea el objeto PWM en el pin 12 con la frecuencia de 1000 Hz.
led_pwm = GPIO.PWM(PIN_LED_PWM, FRECUENCIA_PWM)

# Iniciar el ciclo de trabajo al 0% (LED apagado)
led_pwm.start(0) 

print(f"Programa iniciado. LED en modo 'respiración' en Pin {PIN_LED_PWM}.")
print("Pulsa Ctrl+C para salir.")

try:
    while True:
        # 1. ⬆️ Encendido progresivo (0% a 100%)
        for dc in range(0, 101, INCREMENTO):
            led_pwm.ChangeDutyCycle(dc)
            sleep(TIEMPO_PASO)

        # 2. ⬇️ Apagado progresivo (100% a 0%)
        # Usamos 100 y -1 para incluir el 100 y detenernos en el 0.
        for dc in range(100, -1, -INCREMENTO):
            led_pwm.ChangeDutyCycle(dc)
            sleep(TIEMPO_PASO)

except KeyboardInterrupt:
    print("\nPrograma terminado.")
    
finally:
    # 🚨 Limpieza: Detener el PWM y liberar los pines
    led_pwm.stop() 
    GPIO.cleanup()