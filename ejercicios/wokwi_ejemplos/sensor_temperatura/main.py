"""
Sensor DHT22 - Midiendo Temperatura y Humedad del Aire
===================================================

¿QUÉS ES ESTO?
El DHT22 es un sensor que mide tanto temperatura como humedad en un solo componente.
Es como tener un meteorólogo miniaturizado en tu proyecto, capaz de decirte cuánto
hace de frío o calor y qué tan húmedo está el aire.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes: Sensor DHT22 (temperatura + humedad)

📌 CONEXIONES FÍSICAS (3 cables):
─────────────────────────────────────────────────────────
   GPIO 15 (Pico) ──────► DATA (cable verde/amarillo)
   VBUS (Pico 5V) ──────► VCC (cable rojo)
   GND (Pico) ──────────► GND (cable negro)

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

import machine
import time
import dht

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DEL SENSOR
# ─────────────────────────────────────────────────────────────────────────
# Creamos un objeto DHT22 en el pin GPIO 15
# La librería 'dht' maneja automáticamente la comunicación
sensor = dht.DHT22(machine.Pin(15))


def leer_sensor():
    """
    Lee la temperatura y humedad del sensor DHT22

    Returns:
        tuple: (temperatura, humedad) o None si hay error
    """
    try:
        # medire() activa el sensor y lee los datos
        sensor.measure()

        # Obtener los valores leídos
        temperatura = sensor.temperature()  # Grados Celsius
        humedad = sensor.humidity()  # Porcentaje (0-100)

        return temperatura, humedad

    except OSError as e:
        # Si hay un error de comunicación, lo reportamos
        print(f"⚠️ Error de comunicación: {e}")
        return None


def obtener_clasificacion_temp(temp):
    """
    Traduce una temperatura a una descripción entendible

    Args:
        temp: Temperatura en grados Celsius

    Returns:
        str: Descripción de la temperatura con emoji
    """
    if temp < 10:
        return "🧊 FRÍO - Abrígate!"
    elif temp < 20:
        return "🌤️ FRESCO - Agradable"
    elif temp < 25:
        return "🌡️ CÓMODO - Temperatura ideal"
    elif temp < 30:
        return "🔥 CALIENTE - Cuidado con el calor"
    else:
        return "♨️ MUY CALIENTE - Peligroso!"


def obtener_clasificacion_hum(hum):
    """
    Traduce la humedad a una descripción entendible

    Args:
        hum: Humedad relativa en porcentaje

    Returns:
        str: Descripción de la humedad con emoji
    """
    if hum < 30:
        return "🏜️ SECO - Puede ser incómodo"
    elif hum < 50:
        return "💧 NORMAL - Comfortable"
    elif hum < 70:
        return "💦 HÚMEDO - Un poco pegajoso"
    else:
        return "🌊 MUY HÚMEDO - Como selva tropical"


# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("🌡️ INICIANDO: Sensor DHT22 (Temperatura + Humedad)")
print("   Lectura cada 2 segundos")
print("-" * 50)

while True:
    # Leer el sensor
    resultado = leer_sensor()

    if resultado is not None:
        temperatura, humedad = resultado

        # Obtener clasificaciones amigables
        clasificacion_temp = obtener_clasificacion_temp(temperatura)
        clasificacion_hum = obtener_clasificacion_hum(humedad)

        # Mostrar resultados de forma bonita
        print(f"🌡️ Temperatura: {temperatura:.1f}°C → {clasificacion_temp}")
        print(f"💧 Humedad: {humedad:.1f}% → {clasificacion_hum}")
        print("-" * 50)
    else:
        print("⚠️ Error en lectura, reintentando en 2 segundos...")

    # Esperar 2 segundos antes de la siguiente lectura
    # (el DHT22 necesita al menos 2 segundos entre lecturas)
    time.sleep(2)
