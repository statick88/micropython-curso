"""
Control de Servomotor SG90 - Mover Cosas con Precisión
=====================================================

¿QUÉS ES UN SERVOMOTOR?
Es un motor especial que puede girar a una posición específica (ángulo) y
quedarse ahí. A diferencia de los motores DC que giran libremente, el
servomotor sabe dónde está y puede ir a donde le digas.

El SG90 es el servomotor más popular para proyectos con microcontroladores:
• Tamaño pequeño (como una galleta)
• Barato (menos de $5)
• Rotation: 0° a 180° (media vuelta)
• Fuerza moderada (ideal para proyectos educativos)

📚 CÓMO CONTROLAR UN SERVO:
─────────────────────────────────────────────────────────────────────────
Los servomotores usan una señal especial llamada PWM (Modulación por Ancho
de Pulso). No es tan complicado como suena:

  ┌─────────────────────────────────────────────────────────────────┐
  │ PERÍODO COMPLETO = 20ms (50 Hz)                                 │
  │                                                                  │
  │   0° ──────►│◄── 1ms ───►│◄────────────── 19ms ───►│           │
  │   (mínimo)                          (duty bajo)               │
  │                                                                  │
  │   90° ──────►│◄────── 1.5ms ──────►│◄────────── 18.5ms ──►│    │
  │   (centro)                         (duty medio)               │
  │                                                                  │
  │   180° ─────►│◄────────── 2ms ──────────►│◄──────── 18ms ──►│   │
  │   (máximo)                         (duty alto)                │
  └─────────────────────────────────────────────────────────────────┘

El tiempo del pulso (ancho) determina el ángulo:
• 1ms   → 0°
• 1.5ms → 90°
• 2ms   → 180°

Hardware: ESP32 DevKit V1
Plataforma: Wokwi
Componentes: Servomotor SG90

📌 CONEXIONES FÍSICAS (3 cables):
─────────────────────────────────────────────────────────
  GPIO 13 (ESP32) ──────► SIGNAL (cable amarillo/naranja)
  VCC (ESP32 5V) ───────► VCC (cable rojo)
  GND (ESP32) ──────────► GND (cable marrón/negro)

  ⚠️ IMPORTANTE: El SG90 necesita 5V para funcionar bien. El ESP32
  tiene un pin de 5V (VCC) que刚好 provides lo que necesita.

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

from machine import Pin, PWM
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DEL SERVO
# ─────────────────────────────────────────────────────────────────────────
# El servomotor SG90 usa señal PWM con frecuencia de 50Hz (período de 20ms)
# MicroPython usa valores de duty de 0 a 1023 (10 bits)
#
# Cálculo del duty:
# • 1ms de 20ms = 1/20 = 5% → 5% de 1023 ≈ 51
# • 2ms de 20ms = 2/20 = 10% → 10% de 1023 ≈ 102
#
# Ajustamos experimentally para que funcione bien con el simulador:
SERVO_FRECUENCIA = 50  # 50 Hz → período de 20ms
SERVO_MIN_DUTY = 26  # ~1ms → 0°
SERVO_MAX_DUTY = 123  # ~2ms → 180°
SERVO_DUTY_90 = 77  # ~1.5ms → 90° (centro)

# Configurar el pin GPIO 13 como salida PWM
servo_pin = Pin(13)
servo = PWM(servo_pin)
servo.freq(SERVO_FRECUENCIA)
servo.duty(0)  # Iniciar en 0°


def angulo_a_duty(angulo):
    """
    Convierte un ángulo (0-180) al valor de duty cycle correspondiente

    Esta es una función de MAPEADO (map):
    • Convierte un rango de entrada (0-180) a un rango de salida (min-max)
    • Es como una regla de tres simple
    """
    if angulo < 0:
        angulo = 0
    elif angulo > 180:
        angulo = 180

    # Fórmula: valor_inicial + (porcentaje * rango)
    duty = int(SERVO_MIN_DUTY + (angulo * (SERVO_MAX_DUTY - SERVO_MIN_DUTY) / 180))
    return duty


def mover_servo(angulo):
    """
    Mueve el servomotor a un ángulo específico

    Args:
        angulo: Ángulo en grados (0 a 180)
    """
    # Asegurar que el ángulo esté en el rango válido
    if angulo < 0:
        angulo = 0
    elif angulo > 180:
        angulo = 180

    duty = angulo_a_duty(angulo)
    servo.duty(duty)

    # Mostrar posición en consola (con emoji según ángulo)
    if angulo == 0:
        emoji = "⬅️"
    elif angulo == 90:
        emoji = "⬆️"
    elif angulo == 180:
        emoji = "➡️"
    else:
        emoji = "🔄"

    print(f"{emoji} Servo en: {angulo}° (duty={duty})")


def ejemplo_barrido():
    """Ejemplo 1: Barrido completo - va de un lado a otro"""
    print("\n📖 Ejemplo 1: Barrido completo (ida y vuelta)")
    print("   El servo va de 0° a 180° y luego vuelve a 0°")

    # De 0° a 180° (de 10 en 10)
    for angulo in range(0, 181, 10):
        mover_servo(angulo)
        time.sleep(0.1)  # Pequeña pausa entre cada posición

    # De 180° a 0°
    for angulo in range(180, -1, -10):
        mover_servo(angulo)
        time.sleep(0.1)


def ejemplo_angulos_especificos():
    """Ejemplo 2: Ir a ángulos específicos"""
    print("\n📖 Ejemplo 2: Ángulos específicos")
    print("   Vamos a posiciones predefinidas: 0°, 45°, 90°, 135°, 180°")

    angulos = [0, 45, 90, 135, 180, 90, 0]

    for angulo in angulos:
        mover_servo(angulo)
        time.sleep(1)  # Quedarse 1 segundo en cada posición


def ejemplo_movimiento_suave():
    """Ejemplo 3: Movimiento suave con pasos pequeños"""
    print("\n📖 Ejemplo 3: Movimiento suave (ida y vuelta)")
    print("   Pasos de solo 5° para movimiento más fluido")

    # Ida suave (de 5 en 5)
    for angulo in range(0, 181, 5):
        mover_servo(angulo)
        time.sleep(0.05)  # Pausa más corta = más suave

    # Vuelta suave
    for angulo in range(180, -1, -5):
        mover_servo(angulo)
        time.sleep(0.05)


# ═══════════════════════════════════════════════════════════════════════════
# PROGRAMA PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("🤖 INICIANDO: Control de Servomotor SG90")
print("   Pin GPIO 13 -> Señal PWM")
print("   Rango: 0° a 180°")
print("=" * 50)

time.sleep(2)  # Esperar a que inicie la simulación

# Ejecutar los tres ejemplos en loop
while True:
    ejemplo_barrido()
    time.sleep(1)
    ejemplo_angulos_especificos()
    time.sleep(1)
    ejemplo_movimiento_suave()
    time.sleep(1)
    ejemplo_ir_a()
    time.sleep(1)
    ejemplo_ida_vuelta()
    time.sleep(1)
