"""
Parpadeo de LED - Tu Primer Programa en MicroPython
=====================================================

¿QUÉS ES ESTO?
Este es el clásico "Hello World" de la electrónica. Vamos a hacer que un LED
parpadee cada segundo. Es el punto de partida perfecto para aprender a controlar
硬件 con código.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi (simulador gratuito)
Componentes:
  • 1 LED rojo (el que brilla cuando le damos corriente)
  • 1 resistor de 220Ω (protege el LED de quemarse)
  • Cables de conexión

📌 CONEXIONES FÍSICAS (explicadas para que las entiendas):
─────────────────────────────────────────────────────────
  El LED tiene dos patitas:
    - La más larga es el ÁNODO (+) → se conecta al pin GPIO
    - La más corta es el CÁTODO (-) → se conecta a GND (tierra)

  ¿Por qué un resistor? El LED solo soporta 2V, pero el Pico da 3.3V.
  El resistor de 220Ω limita la corriente para que no se queme.

  WIRE (cableado):
    GPIO 15 (Pico) ────────► ÁNODO del LED (patita larga)
    CÁTODO del LED ──► Resistor 220Ω ──► GND (Pico)

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO (línea por línea)
# ═══════════════════════════════════════════════════════════════════════════

# Importamos las herramientas que vamos a usar
# • Pin: nos permite controlar los pines GPIO (entrada/salida)
# • time: nos permite manejar tiempos (esperas, delays)
from machine import Pin
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DEL LED
# ─────────────────────────────────────────────────────────────────────────
# Aquí ledecimos que el pin GPIO 15 será una SALIDA (OUTPUT)
# Esto significa que podemos CONTROLAR sienvía voltaje o no
led = Pin(15, Pin.OUT)

# El LED está APAGADO inicialmente porque acabamos de configurarlo

# Mensaje inicial por consola (para ver en el monitor serie)
print("🌟 INICIANDO: Parpadeo de LED")
print("   El LED parpadeará cada 1 segundo")
print("   Observa el LED en el simulador y la consola aquí abajo")

# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL (se ejecuta para siempre)
# ═══════════════════════════════════════════════════════════════════════════
while True:
    # Encender el LED
    # Cuando colocamos value(1), el pin GPIO 15 entrega 3.3V (alto)
    led.value(1)
    print("🔴 LED ENCENDIDO")  # Mensaje de debug
    time.sleep(1)  # Mantener el LED prendido por 1 segundo

    # Apagar el LED
    # Cuando colocamos value(0), el pin GPIO 15 entrega 0V (bajo)
    led.value(0)
    print("⚫ LED APAGADO")  # Mensaje de debug
    time.sleep(1)  # Mantener el LED apagado por 1 segundo

# Este bucle se repite infinitamente hasta que desconectes la placa
