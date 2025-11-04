# Cambiamos de territorio y nos adentramos en el
# del sensor de ultrasonido. Tiene la facultad de emitir
# un sonido por un canal y recogerlo por otro si en
# algún momento rebota contra algo. Nos valdremos
# de ello para calcular la distancia entre el sensor y un
# objeto que iremos moviendo de sitio (hacia adelante y
# hacía atrás) de forma que vaya mostrándonos en
# pantalla la distancia que hay en cada momento.



import RPi.GPIO as GPIO
import time

# --- Configuración de Pines ---
# ¡IMPORTANTE! Estos son los números de pines FÍSICOS (modo BOARD).
# Pin 11 Físico = GPIO 17 (anterior BCM)
# Pin 13 Físico = GPIO 27 (anterior BCM)
GPIO_TRIGGER = 11 # Pin de Salida (físico 11)
GPIO_ECHO = 13    # Pin de Entrada (físico 13)

# Ajusta la velocidad del sonido en cm/s (a 20°C es aprox. 34300 cm/s)
VELOCIDAD_SONIDO = 34300 

def medir_distancia():
    # Establecer el Trigger en LOW para asegurar limpieza
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)
    time.sleep(0.000002) # Pequeña pausa de 2 microsegundos

    # 1. Enviar pulso de 10µs a Trigger (para iniciar la medición)
    GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)

    # 2. Capturar el tiempo de inicio (pulso_inicio) cuando el Echo se pone en HIGH
    pulso_inicio = time.time()
    pulso_fin = time.time()
    
    # Esperar a que el pin ECHO se ponga en HIGH (el sensor ha emitido el sonido)
    # Controla para evitar bucles infinitos si hay ruido o error
    timeout_start = time.time()
    while GPIO.input(GPIO_ECHO) == GPIO.LOW:
        pulso_inicio = time.time()
        if pulso_inicio - timeout_start > 0.1:
            return -1 # Retorna un valor de error

    # 3. Capturar el tiempo de fin (pulso_fin) cuando el Echo se pone en LOW
    # (el sensor ha recibido el eco)
    timeout_start = time.time()
    while GPIO.input(GPIO_ECHO) == GPIO.HIGH:
        pulso_fin = time.time()
        if pulso_fin - timeout_start > 0.1:
            return -1 # Retorna un valor de error

    # 4. Calcular la duración del pulso
    duracion = pulso_fin - pulso_inicio

    # 5. Calcular la distancia: (Distancia = (Duración * Velocidad del Sonido) / 2)
    # Se divide por 2 porque la duración incluye el trayecto de ida y vuelta.
    distancia = (duracion * VELOCIDAD_SONIDO) / 2

    return distancia

# --- Configuración Inicial ---
# *** ¡CAMBIO CLAVE! *** Usar la numeración de pines BOARD (física)
GPIO.setmode(GPIO.BOARD) 

# Configurar pines
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # Trigger como salida
GPIO.setup(GPIO_ECHO, GPIO.IN)      # Echo como entrada

print("Iniciando medición de distancia (Modo BOARD)... Presiona Ctrl+C para detener.")
print("-" * 50)

# --- Bucle Principal para Medición Continua ---
try:
    while True:
        distancia_medida = medir_distancia()
        
        # Muestra la distancia si la lectura es válida
        if distancia_medida > 0:
            # Mostrar el resultado en pantalla (redondeado a dos decimales)
            print(f"Distancia: {distancia_medida:.2f} cm")
        else:
            print("⚠️ Error de lectura o sensor fuera de rango.")
        
        # Pausa antes de la siguiente medición
        time.sleep(0.5) 

except KeyboardInterrupt:
    # Bloque para limpiar los pines GPIO al finalizar el programa
    print("\nMedición detenida por el usuario.")
finally:
    GPIO.cleanup()
    print("Pines GPIO limpiados. ¡Adiós!")