"""
Control de Servomotor - ESP32 con MicroPython
============================================
Hardware: ESP32 DevKit V1
Componentes: 1 servomotor SG90
Conexionado: GPIO 13 -> Signal (señal de control)
Lenguaje: MicroPython
Lógica: El servomotor rota entre 0° y 180° continuamente
"""

from machine import Pin, PWM
import time

# Configuración del servomotor
# El servomotor SG90 usa señal PWM con período de 20ms (50Hz)
# Pulso de 1ms = 0°, 1.5ms = 90°, 2ms = 180°
SERVO_FRECUENCIA = 50  # 50 Hz (período de 20ms)
SERVO_MIN_DUTY = 26  # ~1ms (0 grados) - duty cycle mínimo
SERVO_MAX_DUTY = 123  # ~2ms (180 grados) - duty cycle máximo
SERVO_DUTY_90 = 77  # ~1.5ms (90 grados)

# Pin GPIO 13 para control del servo
servo_pin = Pin(13)
servo = PWM(servo_pin)
servo.freq(SERVO_FRECUENCIA)
servo.duty(0)  # Iniciar en 0


def angulo_a_duty(angulo):
    """
    Convierte un ángulo (0-180) a valor de duty cycle

    Args:
        angulo: Ángulo en grados (0-180)

    Returns:
        int: Valor de duty cycle para MicroPython
    """
    # Fórmula lineal: mapear 0-180 a SERVO_MIN_DUTY - SERVO_MAX_DUTY
    duty = int(SERVO_MIN_DUTY + (angulo * (SERVO_MAX_DUTY - SERVO_MIN_DUTY) / 180))
    return duty


def mover_servo(angulo):
    """
    Mueve el servomotor a un ángulo específico

    Args:
        angulo: Ángulo en grados (0-180)
    """
    if angulo < 0:
        angulo = 0
    elif angulo > 180:
        angulo = 180

    duty = angulo_a_duty(angulo)
    servo.duty(duty)
    print(f"🔧 Servo en posición: {angulo}° (duty={duty})")


def ejemplo_barrido():
    """Ejemplo 1: Barrido completo de 0° a 180° y viceversa"""
    print("Ejemplo 1: Barrido completo")

    # De 0° a 180°
    for angulo in range(0, 181, 10):
        mover_servo(angulo)
        time.sleep(0.1)

    # De 180° a 0°
    for angulo in range(180, -1, -10):
        mover_servo(angulo)
        time.sleep(0.1)


def ejemplo_ir_a():
    """Ejemplo 2: Ir a ángulos específicos"""
    print("Ejemplo 2: Ángulos específicos")

    angulos = [0, 45, 90, 135, 180, 90, 0]

    for angulo in angulos:
        mover_servo(angulo)
        time.sleep(1)  # Esperar 1 segundo en cada posición


def ejemplo_ida_vuelta():
    """Ejemplo 3: Ida y vuelta suave"""
    print("Ejemplo 3: Ida y vuelta suave")

    # Ida suave
    for angulo in range(0, 181, 5):
        mover_servo(angulo)
        time.sleep(0.05)

    # Vuelta suave
    for angulo in range(180, -1, -5):
        mover_servo(angulo)
        time.sleep(0.05)


# Mensaje inicial
print("=" * 50)
print("Ejemplo: Control de Servomotor SG90")
print("Pin GPIO 13 -> Signal")
print("Rango: 0° a 180°")
print("=" * 50)

# Programa principal
time.sleep(2)  # Esperar a que inicie la simulación

while True:
    ejemplo_barrido()
    time.sleep(1)
    ejemplo_ir_a()
    time.sleep(1)
    ejemplo_ida_vuelta()
    time.sleep(1)
