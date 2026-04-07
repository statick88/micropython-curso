"""
Sensor de Distancia HC-SR04 - Ejemplo de Entrada Analógica/Digital
================================================================
Hardware: Raspberry Pi Pico con MicroPython
Componentes: 1 sensor ultrasónico HC-SR04
Conexionado: GPIO 2 -> Trigger, GPIO 3 -> Echo
Lenguaje: MicroPython
Lógica: Mide distancia cada 500ms y la muestra por consola
"""

from machine import Pin, time_pulse_us
import time

# Configuración de pines
# Trigger: envía el pulso ultrasónico
trigger = Pin(2, Pin.OUT)
# Echo: recibe el pulso de retorno
echo = Pin(3, Pin.IN)


def medir_distancia():
    """
    Mide la distancia al objeto más cercano usando el sensor HC-SR04

    Returns:
        float: Distancia en centímetros
    """
    # Asegurar que el trigger esté bajo al inicio
    trigger.value(0)
    time.sleep_us(2)

    # Enviar pulso de triggering de 10 microsegundos
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    # Medir el tiempo del pulso de retorno
    # time_pulse_us mide el tiempo entre un cambio de nivel
    try:
        duracion = time_pulse_us(echo, 1, 30000)  # Timeout de 30ms

        # Calcular distancia: tiempo * velocidad del sonido / 2
        # Velocidad del sonido = 343 m/s = 34300 cm/s
        # Distancia = duracion * 34300 / 2 / 1000000
        # Simplificado: distancia = duracion * 0.01715
        distancia = duracion * 0.01715

        return distancia
    except OSError:
        # Timeout: no se detectó objeto dentro del rango
        return -1


def obtener_distancia_formateada():
    """
    Obtiene la distancia y la formatea como string

    Returns:
        str: Distancia formateada o mensaje de error
    """
    distancia = medir_distancia()

    if distancia < 0:
        return "Sin detección"
    elif distancia > 400:
        return "Fuera de rango"
    else:
        return f"{distancia:.2f} cm"


# Mensaje inicial
print("Iniciando sensor de distancia HC-SR04...")
print("Midiendo distancia cada 500ms")

# Bucle principal de medición
while True:
    distancia = medir_distancia()

    if distancia < 0:
        print("⚠️  Sin detección de objeto")
    elif distancia > 400:
        print("📍 Objeto fuera de rango (>400cm)")
    else:
        # Crear representación visual de la distancia
        barras = "█" * int(distancia / 10)
        print(f"📏 Distancia: {distancia:6.2f} cm | {barras}")

    time.sleep(0.5)
