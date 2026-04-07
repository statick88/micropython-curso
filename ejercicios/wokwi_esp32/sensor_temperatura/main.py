"""
Sensor de Temperatura y Humedad DHT22 - ESP32 con MicroPython
=============================================================
Hardware: ESP32 DevKit V1
Componentes: 1 sensor DHT22 (temperatura y humedad)
Conexionado: GPIO 4 -> Data
Lenguaje: MicroPython
Lógica: Lee temperatura y humedad cada 2 segundos
"""

import machine
import time
import dht

# Configuración del sensor DHT22
# Usamos el pin GPIO 4 para la comunicación
sensor = dht.DHT22(machine.Pin(4))


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
print("=" * 50)
print("Ejemplo: Sensor DHT22 con ESP32")
print("Pin: GPIO 4 (Data)")
print("Lectura cada 2 segundos")
print("=" * 50)

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
