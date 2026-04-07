"""
Control de Motor DC - ESP32
===========================
Hardware: ESP32 DevKit V1
Componentes: 1 Motor DC, 1 transistor driver
Conexionado: GPIO 13 -> PWM Motor
Lenguaje: MicroPython
Lógica: Controla velocidad y dirección del motor
"""

from machine import Pin, PWM
import time

# Configuración del motor (GPIO 13)
motor_pin = Pin(13)
motor = PWM(motor_pin)
motor.freq(1000)  # 1kHz PWM
motor.duty(0)  # Iniciar apagado

# Constantes
VELOCIDAD_MIN = 0
VELOCIDAD_MAX = 1023


def iniciar_motor(velocidad):
    """
    Controla la velocidad del motor

    Args:
        velocidad: 0-1023 (0 = detenido, 1023 = máxima)
    """
    if velocidad < 0:
        velocidad = 0
    elif velocidad > VELOCIDAD_MAX:
        velocidad = VELOCIDAD_MAX

    motor.duty(velocidad)
    return velocidad


def ejemplo_rampa():
    """Ejemplo 1: Rampa de velocidad"""
    print("📈 Ejemplo: Rampa de velocidad")
    # Aumentar gradualmente
    for vel in range(0, 1024, 50):
        iniciar_motor(vel)
        print(f"Velocidad: {vel:4d}")
        time.sleep(0.1)

    # Disminuir gradualmente
    for vel in range(1023, -1, -50):
        iniciar_motor(vel)
        print(f"Velocidad: {vel:4d}")
        time.sleep(0.1)

    iniciar_motor(0)
    time.sleep(1)


def ejemplo_niveles():
    """Ejemplo 2: Niveles de velocidad"""
    print("📊 Ejemplo: Niveles de velocidad")
    niveles = [0, 256, 512, 768, 1023, 768, 512, 256, 0]

    for vel in niveles:
        iniciar_motor(vel)
        porcentaje = int((vel / VELOCIDAD_MAX) * 100)
        print(f"Velocidad: {porcentaje:3d}%")
        time.sleep(1)


def ejemplo_pulso():
    """Ejemplo 3: Pulso rápido"""
    print("💨 Ejemplo: Pulso rápido")

    for _ in range(5):
        iniciar_motor(1023)  # Máximo
        print("🚀 MAXIMO")
        time.sleep(0.5)

        iniciar_motor(0)  # Detenido
        print("🛑 PARADO")
        time.sleep(0.5)


def ejemplo_senal():
    """Ejemplo 4: Señal triangular"""
    print("📉 Señal triangular")

    while True:
        # Subir
        for vel in range(0, 1024, 20):
            iniciar_motor(vel)
            time.sleep(0.02)

        # Bajar
        for vel in range(1023, -1, -20):
            iniciar_motor(vel)
            time.sleep(0.02)


# Mensaje inicial
print("=" * 50)
print("Control de Motor DC - ESP32")
print("GPIO 13 -> PWM del motor")
print("=" * 50)

time.sleep(2)

while True:
    ejemplo_rampa()
    time.sleep(1)

    ejemplo_niveles()
    time.sleep(1)

    ejemplo_pulso()
    time.sleep(1)
