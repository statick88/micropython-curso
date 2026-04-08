"""
Sensor PIR - Detectando Movimiento como un Radar Humano
=======================================================

¿QUÉS ES UN SENSOR PIR?
PIR = "Passive InfraRed" (Infrarrojo Pasivo). "Pasivo" porque no emite
nada, solo detecta el calor que emiten los objetos.

Todos los cuerpos emite infrarrojo (IR) - es como "luz invisible" que
no podemos ver pero que nuestros ojos no detectan. El PIR tiene un sensor
especial que capta cambios en esa radiación infrarroja.

📚 CÓMO DETECTA MOVIMIENTO:
─────────────────────────────────────────────────────────────────────────
Imagina que el PIR tiene muchos "ojitos" pequeños que miran en diferentes
direcciones. Cuando una persona (u objeto caliente) pasa:

  1. Primero entra en el "ojito" de la izquierda → detecta más IR
  2. Luego entra en el del medio → detecta aún más
  3. Cuando sale, detecta menos IR

El sensor nota este CAMBIO de calor y dice: "¡Hay movimiento!"

Este sensor se usa en:
• Luces de pasillo que se encienden al pasar
• Sistemas de alarma antirrobos
• Cámaras de seguridad
• Autos que encienden las luces automáticamente

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes:
  • LED (indicador visual)
  • Resistor 220Ω (protege el LED)
  • Sensor PIR HC-SR501 (detector de movimiento)

📌 CONEXIONES FÍSICAS:
─────────────────────────────────────────────────────────
  Para el LED (indicador):
    GPIO 15 ────► ÁNODO LED (patita larga)
    CÁTODO LED ──► Resistor 220Ω ──► GND

  Para el sensor PIR:
    GPIO 16 (Pico) ────► OUTPUT (cable amarillo del PIR)
    VBUS (5V Pico) ────► VCC (cable rojo del PIR)
    GND (Pico) ────────► GND (cable negro del PIR)

  El PIR tiene un potenciómetro para ajustar:
  • Sensibilidad (cuán lejos detecta)
  • Tiempo de retardo (cuánto tiempo da HIGH después de detectar)

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

# LED indicador: nos dice visualmente cuándo hay movimiento
led = Pin(15, Pin.OUT)
led.value(0)  # Iniciar apagado

# Sensor PIR: pin de ENTRADA
# Cuando detecta movimiento, pone este pin en ALTO (3.3V)
# Cuando no hay movimiento, está en BAJO (0V)
pir = Pin(16, Pin.IN)

# Variables para contar y recordar
detecciones = 0  # Cuántas veces se detectó movimiento
ultimo_estado = 0  # Estado anterior del PIR (para detectar cambios)

# Mensaje de inicio
print("🚨 INICIANDO: Sensor de Movimiento PIR HC-SR501")
print("   GPIO 15 → LED indicador")
print("   GPIO 16 → Sensor PIR (detección)")
print("   ¡Mueve tu mano frente al sensor para probarlo!")
print("=" * 50)

# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL - Detectar movimiento
# ═══════════════════════════════════════════════════════════════════════════

while True:
    # Leer el estado actual del sensor PIR
    estado_actual = pir.value()

    # ─────────────────────────────────────────────────────────────────────
    # DETECCIÓN DE FLANCOS (cambios de estado)
    # ─────────────────────────────────────────────────────────────────────

    # FLANCO DE SUBIDA: Pasó de 0 a 1 → ¡Movimiento detectado!
    if estado_actual == 1 and ultimo_estado == 0:
        led.value(1)  # Encender LED como alarma visual
        detecciones += 1
        print(f"🔔 MOVIMIENTO DETECTADO! (#{detecciones})")
        print("   💡 LED ENCENDIDO")

    # FLANCO DE BAJADA: Pasó de 1 a 0 → El movimiento terminó
    elif estado_actual == 0 and ultimo_estado == 1:
        led.value(0)  # Apagar LED
        print("✅ Movimiento terminado")
        print("   💡 LED APAGADO")
        print("-" * 40)

    # Recordar el estado para la siguiente iteración
    ultimo_estado = estado_actual

    # Pequeña pausa para no saturar el procesador
    time.sleep(0.1)
