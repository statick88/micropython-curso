"""
Parpadeo de LED - ESP32 con MicroPython
=======================================
Tu segundo proyecto: ahora con un microcontrolador diferente

¿QUÉS ES ESTO?
El mismo proyecto del LED parpadeante, pero ahora usamos el ESP32 en lugar
del Raspberry Pi Pico. Verás que es muy similar, ¡solo cambia el pin!

Hardware: ESP32 DevKit V1 (la placa azul con antenita WiFi)
Plataforma: Wokwi
Componentes:
  • 1 LED rojo
  • 1 resistor de 220Ω (protege el LED)

📌 CONEXIONES FÍSICAS:
─────────────────────────────────────────────────────────
  GPIO 2 (ESP32) ───────► ÁNODO del LED (patita larga)
  CÁTODO del LED ──► Resistor 220Ω ──► GND (ESP32)

  ¿Por qué GPIO 2? Porque es el pin del LED integrado (azul) en la placa.
  Aunque usamos un LED externo, usamos el mismo pin para mantenerlo simple.

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

from machine import Pin
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DEL LED
# ─────────────────────────────────────────────────────────────────────────
# GPIO 2: En el ESP32, este pin está conectado al LED azul integrado
# También funciona perfectamente para controlar un LED externo
led = Pin(2, Pin.OUT)

# Mensaje inicial con formato bonito
print("=" * 50)
print("🌟 EJEMPLO: Parpadeo de LED con ESP32")
print("   Pin GPIO 2 configurado como salida")
print("   El LED parpadeará cada 1 segundo")
print("=" * 50)

# Bucle principal con contador
contador = 0
while True:
    led.value(1)  # Encender LED (3.3V)
    print(f"[{contador:02d}] 🔴 LED ENCENDIDO")
    time.sleep(1)

    led.value(0)  # Apagar LED (0V)
    print(f"[{contador:02d}] ⚫ LED APAGADO")
    time.sleep(1)

    contador += 1  # Incrementar contador cada ciclo
