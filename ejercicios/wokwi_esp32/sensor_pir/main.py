"""
Sensor PIR - Detectando Movimiento como un Radar Humano (ESP32)
==============================================================

¿QUÉS ES UN SENSOR PIR?
PIR = "Passive InfraRed" (Infrarrojo Pasivo). Es un sensor que detecta
el calor emitido por los cuerpos (personas, animales, objetos calientes).

Cuando alguien se mueve frente al sensor, cambia la cantidad de infrarrojo
que llega al sensor, y eso lo detecta como "movimiento".

📚 CÓMO FUNCIONA:
─────────────────────────────────────────────────────────────────────────
El sensor PIR HC-SR501 tiene dos potenciómetros:
• Sensibilidad: qué tan lejos detecta (3-7 metros)
• Tiempo: cuánto tiempo permanece en ALTO después de detectar

Su comportamiento:
• Detecta movimiento → salida = ALTO (3.3V)
• No hay movimiento → salida = BAJO (0V)

Se usa en:
• Luces automático de pasillos
• Sistemas de alarma
• Cámaras de seguridad
• Autos (luces automáticas)

Hardware: ESP32 DevKit V1
Plataforma: Wokwi
Componentes: LED, resistor 220Ω, sensor PIR HC-SR501

📌 CONEXIONES FÍSICAS:
─────────────────────────────────────────────────────────
  LED indicador (GPIO 2 - LED integrado del ESP32):
    GPIO 2 ────► ÁNODO LED
    CÁTODO ──► Resistor 220Ω ──► GND

  Sensor PIR:
    GPIO 18 (ESP32) ────► OUTPUT (cable amarillo)
    VCC (5V ESP32) ──────► VCC (cable rojo)
    GND (ESP32) ─────────► GND (cable negro)

  El ESP32 tiene un LED azul integrado en GPIO 2, que usamos como indicador.
  El sensor PIR necesita 5V para funcionar bien.

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

# LED en GPIO 2 (el LED azul integrado del ESP32)
led = Pin(2, Pin.OUT)
led.value(0)  # Apagado al inicio

# Sensor PIR en GPIO 18
pir = Pin(18, Pin.IN)

# Variables de estado
detecciones = 0  # Contador de detecciones
ultimo_estado = 0  # Estado anterior del sensor

# Mensaje inicial
print("🚨 INICIANDO: Sensor PIR en ESP32")
print("   GPIO 2 → LED indicador (azul integrado)")
print("   GPIO 18 → Sensor PIR")
print("   ¡Mueve tu mano frente al sensor para probar!")
print("=" * 50)

# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL - Detectar movimiento
# ═══════════════════════════════════════════════════════════════════════════

while True:
    # Leer estado actual del sensor
    estado_actual = pir.value()

    # Detectar INICIO de movimiento (flanco de subida: 0 → 1)
    if estado_actual == 1 and ultimo_estado == 0:
        led.value(1)  # Encender LED
        detecciones += 1
        print(f"🔔 MOVIMIENTO DETECTADO! (#{detecciones})")

    # Detectar FIN de movimiento (flanco de bajaa: 1 → 0)
    elif estado_actual == 0 and ultimo_estado == 1:
        led.value(0)  # Apagar LED
        print("✅ Movimiento terminado")
        print("-" * 40)

    # Actualizar estado para la siguiente iteración
    ultimo_estado = estado_actual

    # Pausa pequeña para no saturar el CPU
    time.sleep(0.1)
