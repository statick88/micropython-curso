"""
Sensor Hall Efecto - Detectando Campos Magnéticos
=================================================

¿QUÉS ES ESTO?
El sensor Hall detecta la presencia de campos magnéticos sin necesidad de
contacto físico. Funciona como un "interruptor invisible" que se activa
cuando se acerca un imán. Es ampliamente utilizado en velocímetros,
sistemas de frenado ABS y detectores de posición.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes: Sensor Hall KY-024

📌 CONEXIONES FÍSICAS (3 cables):
─────────────────────────────────────────────────────────
   • VCC (sensor) ────────► 3.3V (Pico) - cable rojo
   • GND (sensor) ────────► GND (Pico)  - cable negro
   • OUT (sensor) ────────► GPIO 2 (Pico) - cable amarillo

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

from machine import Pin
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE PINES
# ─────────────────────────────────────────────────────────────────────────

# LED: nos dice cuando se detecta el imán
led = Pin(15, Pin.OUT)
led.value(0)  # Apagado al inicio

# Sensor Hall en GPIO 16
# Es una entrada digital: 1 = detecta imán, 0 = no detecta
hall = Pin(16, Pin.IN)

# Variables para contar detecciones
detecciones = 0  # Cuántas veces se detectó el imán
ultimo_estado = 0  # Estado anterior (para detectar cambios)

# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("🧲 INICIANDO: Sensor de Efecto Hall")
print("   GPIO 15 → LED indicador")
print("   GPIO 16 → Sensor Hall")
print("   ¡Acerca un imán para probar!")
print("=" * 50)

while True:
    # Leer el estado actual del sensor (0 o 1)
    estado_actual = hall.value()

    # Detectar cuando el imán se ACERCA (flanco de subida: 0 → 1)
    if estado_actual == 1 and ultimo_estado == 0:
        led.value(1)  # Encender LED
        detecciones += 1
        print(f"🧲 IMÁN DETECTADO! (#{detecciones})")
        print("   ✅ Campo magnético presente")
        print("   💡 LED ENCENDIDO")

    # Detectar cuando el imán se ALEJA (flanco de bajaa: 1 → 0)
    elif estado_actual == 0 and ultimo_estado == 1:
        led.value(0)  # Apagar LED
        print("✅ Imán retirado")
        print("   ❌ Campo magnético ausente")
        print("   💡 LED APAGADO")
        print("-" * 40)

    # Recordar el estado para la próxima iteración
    ultimo_estado = estado_actual

    # Pequeña pausa para no saturar el CPU
    time.sleep(0.1)
