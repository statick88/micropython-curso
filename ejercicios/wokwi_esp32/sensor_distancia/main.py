"""
Sensor de Distancia HC-SR04 - ESP32 con MicroPython
==================================================
Hardware: ESP32 DevKit V1
Componentes: 1 sensor ultrasónico HC-SR04
Conexionado: GPIO 5 -> Trigger, GPIO 18 -> Echo
Lenguaje: MicroPython
Lógica: Mide distancia cada 500ms y la muestra por consola
"""

from machine import Pin, time_pulse_us
import time

# Configuración de pines
# Trigger: envía el pulso ultrasónico
trigger = Pin(5, Pin.OUT)
# Echo: recibe el pulso de retorno
echo = Pin(18, Pin.IN)


def medir_distancia():
    """
    Mide la distancia al objeto más cercano usando el sensor HC-SR04

    Returns:
        float: Distancia en centímetros, -1 si hay error
    """
    # Asegurar que el trigger esté bajo al inicio
    trigger.value(0)
    time.sleep_us(2)

    # Enviar pulso de triggering de 10 microsegundos
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    # Medir el tiempo del pulso de retorno
    try:
        # time_pulse_us(clk_level, timeout_us)
        # Devuelve el tiempo en microsegundos
        duracion = time_pulse_us(echo, 1, 30000)  # Timeout de 30ms

        # Calcular distancia:
        # Velocidad del sonido = 343 m/s = 0.0343 cm/μs
        # Distancia = tiempo × velocidad / 2 (ida y vuelta)
        distancia = duracion * 0.0343 / 2

        return distancia
    except OSError:
        # Timeout: no se detectó objeto dentro del rango
        return -1


# Mensaje inicial
print("=" * 50)
print("Ejemplo: Sensor de Distancia HC-SR04")
print("Pines: GPIO 5 (Trigger), GPIO 18 (Echo)")
print("=" * 50)

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
