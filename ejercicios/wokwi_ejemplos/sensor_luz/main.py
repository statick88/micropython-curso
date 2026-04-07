"""
Sensor de Luz LDR - Raspberry Pi Pico
====================================
Hardware: Raspberry Pi Pico
Componentes: 1 LED, 1 resistencia, 1 fotorresistor (LDR)
Conexionado: GPIO 15 -> LED, GPIO 26 -> LDR (ADC)
Lenguaje: MicroPython
Lógica: LED se enciende cuando hay poca luz
"""

from machine import Pin, ADC
import time

# Configuración de pines
# LED en GPIO 15
led = Pin(15, Pin.OUT)
led.value(0)

# LDR en GPIO 26 (ADC)
# El LDR varía su resistencia según la luz
# Más luz = menor resistencia = mayor voltaje
ldr = ADC(Pin(26))

# Constantes
UMBRAL_OSCURO = 1500  # Valor para considerar "oscuro"
UMBRAL_LUZ = 3000  # Valor para considerar "con luz"


def leer_luz():
    """Lee el valor del sensor LDR"""
    return ldr.read()


def obtener_nivel_luz(valor):
    """Retorna una clasificación del nivel de luz"""
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
print("Sensor de Luz LDR")
print("GPIO 15 -> LED, GPIO 26 -> LDR (ADC)")
print("=" * 50)

# Bucle principal
while True:
    # Leer valor del LDR
    valor = leer_luz()
    nivel = obtener_nivel_luz(valor)

    # Determinar si activar el LED
    if valor < UMBRAL_OSCURO:
        led.value(1)  # Encender LED (está oscuro)
        estado_led = "💡 ENCENDIDO"
    else:
        led.value(0)  # Apagar LED (hay luz)
        estado_led = "⚫ APAGADO"

    # Mostrar información
    print(f"Valor LDR: {valor:4d} | Nivel: {nivel} | LED: {estado_led}")

    # Representación visual
    barras = "█" * int(valor / 500)
    print(f"  Luz: {barras}")
    print("-" * 40)

    time.sleep(0.2)
