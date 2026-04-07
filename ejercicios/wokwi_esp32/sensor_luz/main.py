"""
Sensor de Luz LDR - ESP32
=========================
Hardware: ESP32 DevKit V1
Componentes: 1 LED, 1 resistencia, 1 fotorresistor (LDR)
Conexionado: GPIO 2 -> LED, GPIO 34 -> LDR (ADC)
Lenguaje: MicroPython
Lógica: LED se enciende cuando hay poca luz
"""

from machine import Pin, ADC
import time

# Configuración de pines
# LED en GPIO 2
led = Pin(2, Pin.OUT)
led.value(0)

# LDR en GPIO 34 (ADC)
ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)  # Rango completo 0-3.3V

# Constantes
UMBRAL_OSCURO = 1500


def leer_luz():
    """Lee el valor del sensor LDR"""
    return ldr.read()


def obtener_nivel_luz(valor):
    """Clasificación del nivel de luz"""
    if valor < 1000:
        return "🌑 OSCURO"
    elif valor < 2000:
        return "🌤️ PENUMBRA"
    elif valor < 3500:
        return "☀️ NORMAL"
    else:
        return "💡 MUY BRILLANTE"


# Mensaje inicial
print("=" * 50)
print("Sensor de Luz LDR - ESP32")
print("GPIO 2 -> LED, GPIO 34 -> LDR (ADC)")
print("=" * 50)

# Bucle principal
while True:
    valor = leer_luz()
    nivel = obtener_nivel_luz(valor)

    if valor < UMBRAL_OSCURO:
        led.value(1)
        estado_led = "💡 ENCENDIDO"
    else:
        led.value(0)
        estado_led = "⚫ APAGADO"

    print(f"Valor LDR: {valor:4d} | Nivel: {nivel} | LED: {estado_led}")

    barras = "█" * int(valor / 500)
    print(f"  Luz: {barras}")
    print("-" * 40)

    time.sleep(0.2)
