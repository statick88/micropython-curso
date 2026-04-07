"""
Control de Relé - ESP32
======================
Hardware: ESP32 DevKit V1
Componentes: 1 LED, 1 resistor, 1 módulo relé
Conexionado: GPIO 2 -> LED, GPIO 19 -> Relé
Lenguaje: MicroPython
Lógica: Controla un relé
"""

from machine import Pin
import time

# Configuración
led = Pin(2, Pin.OUT)
led.value(0)

rele = Pin(19, Pin.OUT)
rele.value(1)

cambios = 0


def activar():
    rele.value(0)
    led.value(1)
    print("🔋 RELÉ ACTIVADO")


def desactivar():
    rele.value(1)
    led.value(0)
    print("⭕ RELÉ DESACTIVADO")


print("=" * 50)
print("Control de Relé - ESP32")
print("GPIO 2 -> LED, GPIO 19 -> Relé")
print("=" * 50)

while True:
    activar()
    cambios += 1
    print(f"👉 Cambio #{cambios}: ON por 2s")
    time.sleep(2)

    desactivar()
    cambios += 1
    print(f"👉 Cambio #{cambios}: OFF por 2s")
    time.sleep(2)
