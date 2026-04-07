"""
Sensor de Temperatura y Humedad DHT22 - Ejemplo de Entrada Digital
================================================================
Hardware: Raspberry Pi Pico con MicroPython
Componentes: 1 sensor DHT22 (temperatura y humedad)
Conexionado: GPIO 15 -> Data
Lenguaje: MicroPython
Lógica: Lee temperatura y humedad cada 2 segundos
"""

import machine
import time
import dht

# Configuración del sensor DHT22
# Usamos el pin GPIO 15 para la comunicación
sensor = dht.DHT22(machine.Pin(15))


def leer_sensor():
    """
    Lee los valores del sensor DHT22

    Returns:
        tuple: (temperatura, humedad) o None si hay error
    """
    try:
        sensor.measure()
        temperatura = sensor.temperature()
        humedad = sensor.humidity()
        return temperatura, humedad
    except OSError as e:
        print(f"Error de lectura: {e}")
        return None


def obtener_clasificacion_temp(temp):
    """
    Obtiene una clasificación textual de la temperatura

    Args:
        temp: Temperatura en grados Celsius

    Returns:
        str: Clasificación de la temperatura
    """
    if temp < 10:
        return "🧊 FRÍO"
    elif temp < 20:
        return "🌤️ FRESCO"
    elif temp < 25:
        return "🌡️ CÓMODO"
    elif temp < 30:
        return "🔥 CALIENTE"
    else:
        return "♨️ MUY CALIENTE"


def obtener_clasificacion_hum(hum):
    """
    Obtiene una clasificación textual de la humedad

    Args:
        hum: Humedad relativa en porcentaje

    Returns:
        str: Clasificación de la humedad
    """
    if hum < 30:
        return "🏜️ SECO"
    elif hum < 50:
        return "💧 NORMAL"
    elif hum < 70:
        return "💦 HÚMEDO"
    else:
        return "🌊 MUY HÚMEDO"


# Mensaje inicial
print("Iniciando sensor DHT22...")
print("Lectura de temperatura y humedad cada 2 segundos")

# Bucle principal de lectura
while True:
    resultado = leer_sensor()

    if resultado is not None:
        temperatura, humedad = resultado

        # Obtener clasificaciones
        cla_temp = obtener_clasificacion_temp(temperatura)
        cla_hum = obtener_clasificacion_hum(humedad)

        # Mostrar resultados formateados
        print(f"🌡️  Temperatura: {temperatura}°C - {cla_temp}")
        print(f"💧  Humedad: {humedad}% - {cla_hum}")
        print("-" * 50)
    else:
        print("⚠️  Error al leer el sensor, reintentando...")

    # Esperar 2 segundos entre lecturas
    time.sleep(2)
