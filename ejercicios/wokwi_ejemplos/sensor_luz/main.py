"""
Sensor de Luz LDR - Tu Microcontrolador Ve la Luz
===============================================

¿QUÉS ES ESTO?
El sensor LDR (Light Dependent Resistor) es como un "ojo electrónico" que mide cuánta luz hay en el ambiente. Su resistencia cambia según la luz: con mucha luz deja pasar más corriente, con poca luz deja pasar menos. Es perfecto para crear luces que se encienden automáticamente al anochecer o robots que siguen líneas blancas.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes:
   • LED indicador + resistor 220Ω
   • Fotorresistencia LDR (tipo GL5528 o similar)
   • Resistor de 10kΩ (para el divisor de voltaje)

📌 CONEXIONES FÍSICAS:
─────────────────────────────────────────────────────────
   LED indicador:
     GPIO 15 ────► ÁNODO LED
     CÁTODO LED ──► Resistor 220Ω ──► GND

   Sensor LDR (divisor de voltaje):
     GPIO 26 (Pico) ────► Punto medio del divisor (señal)
     3.3V (Pico) ───────► Un extremo del LDR
     GPIO 26 ───────────► Resistor 10kΩ ──► GND
     El otro extremo del LDR ──► GND

   En Wokwi, el componente LDR ya incluye el resistor, solo conectamos:
     GPIO 26 → LDR signal
     VCC 3.3V → LDR VCC
     GND → LDR GND

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

from machine import Pin, ADC
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE PINES
# ─────────────────────────────────────────────────────────────────────────

# LED: se enciende cuando está oscuro (luz de emergencia)
led = Pin(15, Pin.OUT)
led.value(0)  # Apagado al inicio

# LDR en GPIO 26 (pin ADC del Pico)
# Lee valores analógicos: más luz = número más alto
ldr = ADC(Pin(26))

# Umbrales para decidir cuándo es "oscuro"
# Ajusta estos valores según tu ambiente
UMBRAL_OSCURO = 1500  # Menor que esto = oscuro → prender LED
UMBRAL_LUZ = 3000  # Referencia para "mucha luz"


def leer_luz():
    """
    Lee el nivel de luz del sensor LDR

    Returns:
        int: Valor de 0 (oscuridad total) a 4095 (máxima luz)
    """
    return ldr.read()


def obtener_nivel_luz(valor):
    """
    Traduce el valor numérico a una descripción entendible

    Args:
        valor: Lectura del LDR (0-4095)

    Returns:
        str: Descripción del nivel de luz con emoji
    """
    if valor < 1000:
        return "🌑 OSCURO - Noche o sombra"
    elif valor < 2000:
        return "🌤️ PENUMBRA - Luz tenue"
    elif valor < 3500:
        return "☀️ NORMAL - Luz de habitación"
    else:
        return "💡 MUY BRILLANTE - Sol directo"


# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("☀️ INICIANDO: Sensor de Luz LDR")
print("   GPIO 15 → LED (se prende cuando está oscuro)")
print("   GPIO 26 → Sensor LDR (lectura analógica)")
print("=" * 50)

while True:
    # Leer el nivel de luz actual
    valor_actual = leer_luz()
    nivel = obtener_nivel_luz(valor_actual)

    # Decidir si prender el LED
    if valor_actual < UMBRAL_OSCURO:
        # Está oscuro → prender LED como luz de emergencia
        led.value(1)
        estado_led = "💡 ENCENDIDO (modo noche)"
    else:
        # Hay suficiente luz → apagar LED
        led.value(0)
        estado_led = "⚫ APAGADO (hay luz)"

    # Mostrar información en consola
    print(f"📊 Lectura: {valor_actual:4d} | Nivel: {nivel}")
    print(f"   LED: {estado_led}")

    # Representación visual con barras (cada 500 puntos = █)
    barras = "█" * int(valor_actual / 500)
    print(f"   Intensidad: {barras}")
    print("-" * 40)

    # Pausa entre lecturas (200ms)
    time.sleep(0.2)
