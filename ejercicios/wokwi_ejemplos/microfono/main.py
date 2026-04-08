"""
Micrófono KY-038 - Detectando Sonido y Vibraciones
=================================================

¿QUÉS ES ESTO?
El micrófono KY-038 es un sensor que detecta ondas sonoras y las convierte
en una señal eléctrica que podemos medir. Es como un "oído electrónico" que
nos permite medir el nivel de ruido ambiental o detectar golpes y vibraciones.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes: Micrófono KY-038

📌 CONEXIONES FÍSICAS (3 cables):
─────────────────────────────────────────────────────────
   • VCC (micrófono) ────────► 3.3V (Pico) - cable rojo
   • GND (micrófono) ────────► GND (Pico)  - cable negro
   • OUT (micrófono) ────────► GPIO 26 (ADC0) (Pico) - cable amarillo

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

# LED indicador: se enciende cuando hay sonido
led = Pin(15, Pin.OUT)
led.value(0)  # Apagado al inicio

# Micrófono en GPIO 26 (uno de los pines ADC del Pico)
# ADC significa que puede leer valores analógicos (no solo 0/1)
microfono = ADC(Pin(26))

# Umbral: valor mínimo para considerar que hay "sonido"
# Ajustamos a 2000 para detectar conversaciones normales
UMBRAL_SONIDO = 2000


def leer_sonido():
    """
    Lee el nivel de sonido del micrófono

    Returns:
        int: Valor de 0 (silencio) a 4095 (sonido muy fuerte)
    """
    return microfono.read()


# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL - Detectar sonidos
# ═══════════════════════════════════════════════════════════════════════════

print("🎤 INICIANDO: Detector de Sonido")
print("   GPIO 15 → LED indicador")
print("   GPIO 26 → Micrófono (ADC)")
print("   ¡Haz ruido para activar el LED!")
print("=" * 50)

sonido_maximo = 0  # Para registrar el sonido más alto detectado

while True:
    # Leer el nivel de sonido actual
    nivel_actual = leer_sonido()

    # Registrar el máximo para referencia
    if nivel_actual > sonido_maximo:
        sonido_maximo = nivel_actual

    # Decidir si hay sonido o no
    if nivel_actual > UMBRAL_SONIDO:
        # ¡Hay sonido suficiente!
        led.value(1)  # Encender LED
        print(f"🔊 SONIDO DETECTADO! (nivel: {nivel_actual})")

        # Mostrar representación visual con barras
        # Cada 200 puntos = un bloque █
        barras = "█" * int(nivel_actual / 200)
        print(f"   📊 Intensidad: {barras}")
    else:
        # Silencio o sonido muy bajo
        led.value(0)  # Apagar LED

    # Pequeña pausa entre lecturas
    time.sleep(0.05)
