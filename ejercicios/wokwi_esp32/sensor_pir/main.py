"""
Sensor PIR (Movimiento) - ESP32
===============================
Hardware: ESP32 DevKit V1
Componentes: 1 LED, 1 resistor, 1 sensor PIR
Conexionado: GPIO 2 -> LED, GPIO 18 -> PIR
Lenguaje: MicroPython
Lógica: Detecta movimiento
"""

from machine import Pin
import time

# Configuración
led = Pin(2, Pin.OUT)
led.value(0)

pir = Pin(18, Pin.IN)

detecciones = 0
ultimo_estado = 0

print("=" * 50)
print("Sensor PIR - ESP32")
print("GPIO 2 -> LED, GPIO 18 -> PIR")
print("=" * 50)

while True:
    estado = pir.value()

    if estado == 1 and ultimo_estado == 0:
        led.value(1)
        detecciones += 1
        print(f"🚨 MOVIMIENTO! (#{detecciones})")

    elif estado == 0 and ultimo_estado == 1:
        led.value(0)
        print("✅ Fin de movimiento")
        print("-" * 40)

    ultimo_estado = estado
    time.sleep(0.1)
