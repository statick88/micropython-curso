"""
Micrófono - Raspberry Pi Pico
=============================
Hardware: Raspberry Pi Pico
Componentes: 1 LED, 1 resistor, 1 módulo麦克风
Conexionado: GPIO 15 -> LED, GPIO 26 -> Micrófono (ADC)
Lenguaje: MicroPython
Lógica: Detecta sonidos y enciende LED cuando hay ruido
"""

from machine import Pin, ADC
import time

# Configuración de pines
led = Pin(15, Pin.OUT)
led.value(0)

# Micrófono en GPIO 26 (ADC)
microfono = ADC(Pin(26))

# Umbral para detectar sonido
UMBRAL_SONIDO = 2000


def leer_sonido():
    """Lee el nivel de sonido del micrófono"""
    return microfono.read()


# Mensaje inicial
print("=" * 50)
print("Detector de Sonido (Micrófono)")
print("GPIO 15 -> LED, GPIO 26 -> Micrófono (ADC)")
print("Haz ruido para activar el LED!")
print("=" * 50)

# Variables
sonido_maximo = 0

# Bucle principal
while True:
    valor = leer_sonido()

    # Actualizar máximo
    if valor > sonido_maximo:
        sonido_maximo = valor

    # Detectar sonido
    if valor > UMBRAL_SONIDO:
        led.value(1)
        print(f"🔊 SONIDO DETECTADO! Valor: {valor}")
    else:
        led.value(0)

    # Mostrar cada 20 lecturas
    if valor > UMBRAL_SONIDO:
        barras = "█" * int(valor / 200)
        print(f"  Nivel: {barras}")

    time.sleep(0.05)
