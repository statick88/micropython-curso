"""
Motor DC - Controlando Velocidad con PWM
========================================

¿QUÉS ES UN MOTOR DC?
DC = "Direct Current" (Corriente Continua). Es el motor más simple:
le das voltaje y gira. Quitas el voltaje y se detiene.

Los motores DC se usan en:
• Robots con ruedas
• Ventiladores
• Juguetes (autitos, helicópteros)
• Máquinas industriales

📚 CÓMO CONTROLAR LA VELOCIDAD:
─────────────────────────────────────────────────────────────────────────
No podemos controlar un motor directamente con un pin GPIO porque:

1. El GPIO solo puede dar 3.3V y pocos miliamperios
2. El motor puede necesitar 12V, 24V o más
3. El motor puede consumir amperios, no miliamperios

SOLUCIÓN: Usamos un "driver" (transistor) o modulamos el voltaje con PWM.

📚 QUÉ ES PWM:
─────────────────────────────────────────────────────────────────────────
PWM = "Pulse Width Modulation" (Modulación por Ancho de Pulso)

Es como prender y apagar el motor muy rápido:
• Si está prendido 50% del tiempo → motor gira a media velocidad
• Si está prendido 100% del tiempo → motor gira a toda velocidad
• Si está prendido 0% → motor apagado

         100% (máximo)          50% (medio)           0% (apagado)
    ────┐     ┌─────┐       ┌───┐     ┌───┐
        │     │     │       │   │     │   │
        └─────┘     └       └───┘     └───┘
     ┌─────────┐         ┌─────┐       (apagado)
     │         │
     └─────────┘

El microcontrolador puede hacer esto automáticamente con PWM.

⚠️ IMPORTANTE: En un proyecto real, necesitas un transistor (como el
TIP120) o un driver (L298N, DRV8833) para manejar el motor. En Wokwi
el motor ya tiene un driver incorporado.

Hardware: ESP32 DevKit V1
Plataforma: Wokwi
Componentes: Motor DC (con driver integrado en la simulación)

📌 CONEXIONES FÍSICAS:
─────────────────────────────────────────────────────────
  En Wokwi es很简单 (driver ya incluido):
    GPIO 13 (ESP32) ────► SIGNAL del motor
    VCC (5V ESP32) ──────► VCC del motor
    GND (ESP32) ─────────► GND del motor

  En proyecto REAL necesitarías:
    ESP32 GPIO 13 ──► Driver (ej: L298N) ──► Motor
    VCC 12V ────────► Driver ──► Motor
    GND ───────────► Driver y Motor

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

from machine import Pin, PWM
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DEL MOTOR
# ─────────────────────────────────────────────────────────────────────────

# GPIO 13 controla el motor con señal PWM
motor_pin = Pin(13)
motor = PWM(motor_pin)

# Frecuencia de 1kHz (estándar para motores DC)
motor.freq(1000)

# Iniciar apagado (duty 0)
motor.duty(0)

# Rango de velocidad (MicroPython PWM usa 0-1023)
VELOCIDAD_MIN = 0
VELOCIDAD_MAX = 1023


def iniciar_motor(velocidad):
    """
    Establece la velocidad del motor

    Args:
        velocidad: Valor de 0 a 1023
                   0 = detenido
                   512 = ~50% velocidad
                   1023 = máxima velocidad
    """
    # Asegurar que esté en el rango válido
    if velocidad < VELOCIDAD_MIN:
        velocidad = VELOCIDAD_MIN
    elif velocidad > VELOCIDAD_MAX:
        velocidad = VELOCIDAD_MAX

    motor.duty(velocidad)
    return velocidad


# ═══════════════════════════════════════════════════════════════════════════
# EJEMPLOS DE CONTROL
# ═══════════════════════════════════════════════════════════════════════════


def ejemplo_rampa():
    """
    Ejemplo 1: Rampa gradual

    Aumenta la velocidad poco a poco, luego disminuye.
    Esto muestra el control analógico del motor.
    """
    print("📈 EJEMPLO 1: Rampa de Velocidad")
    print("   Aumentando gradualmente...")

    # Aumentar de 0 a 1023 (de 50 en 50)
    for velocidad in range(0, 1024, 50):
        iniciar_motor(velocidad)
        print(f"   Velocidad: {velocidad:4d} / 1023")
        time.sleep(0.1)

    print("   Disminuyendo gradualmente...")

    # Disminuir de 1023 a 0
    for velocidad in range(1023, -1, -50):
        iniciar_motor(velocidad)
        print(f"   Velocidad: {velocidad:4d} / 1023")
        time.sleep(0.1)

    # Apagar al final
    iniciar_motor(0)
    time.sleep(1)


def ejemplo_niveles():
    """
     Ejemplo 2: Niveles predefinidos

    Vamos a velocidades específicas: 0%, 25%, 50%, 75%, 100%
    """
    print("📊 EJEMPLO 2: Niveles de Velocidad")

    # Niveles en porcentaje: 0%, 25%, 50%, 75%, 100%, 75%, 50%, 25%, 0%
    niveles = [0, 256, 512, 768, 1023, 768, 512, 256, 0]

    for vel in niveles:
        iniciar_motor(vel)
        porcentaje = int((vel / VELOCIDAD_MAX) * 100)
        print(f"   Velocidad: {porcentaje:3d}%")
        time.sleep(1)


def ejemplo_pulso():
    """
    Ejemplo 3: Pulso ON/OFF

    Alternar entre máxima velocidad y apagado.
    Útil para señales de advertencia o blinks.
    """
    print("💨 EJEMPLO 3: Pulso Rápido")

    for _ in range(5):
        iniciar_motor(1023)  # Máxima velocidad
        print("   🚀 MOTOR A TODA VELOCIDAD")
        time.sleep(0.5)

        iniciar_motor(0)  # Detenido
        print("   🛑 MOTOR DETENIDO")
        time.sleep(0.5)


def ejemplo_senal_triangular():
    """
    Ejemplo 4: Señal triangular continua

    Velocidad que sube y baja suavemente en un ciclo infinito.
    """
    print("📈 EJEMPLO 4: Señal Triangular (continuo)")
    print("   Presiona STOP en Wokwi para detener")

    while True:
        # Subir suavemente
        for vel in range(0, 1024, 20):
            iniciar_motor(vel)
            time.sleep(0.02)

        # Bajar suavemente
        for vel in range(1023, -1, -20):
            iniciar_motor(vel)
            time.sleep(0.02)


# ═══════════════════════════════════════════════════════════════════════════
# PROGRAMA PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("⚙️ INICIANDO: Control de Motor DC")
print("   Pin GPIO 13 → Señal PWM")
print("   Rango: 0 (apagado) a 1023 (máximo)")
print("=" * 50)

time.sleep(2)  # Esperar a que cargue la simulación

# Ejecutar ejemplos en loop
while True:
    ejemplo_rampa()
    time.sleep(1)

    ejemplo_niveles()
    time.sleep(1)

    ejemplo_pulso()
    time.sleep(1)

    # El ejemplo 4 es infinito, descomenta para usarlo:
    # ejemplo_senal_triangular()
