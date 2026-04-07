"""
Potenciómetro Controlando LED - ESP32 con MicroPython
=====================================================
Hardware: ESP32 DevKit V1
Componentes: 1 LED, 1 resistor 220Ω, 1 potenciómetro
Conexionado: GPIO 2 -> LED, GPIO 34 -> ADC (potenciómetro)
Lenguaje: MicroPython
Lógica: El brillo del LED varía según la posición del potenciómetro
"""

from machine import Pin, ADC, PWM
import time

# Configuración de pines
# LED en GPIO 2 como salida PWM (para modulate brillo)
led = Pin(2, Pin.OUT)
led_pwm = PWM(led)
led_pwm.freq(1000)  # Frecuencia PWM 1kHz
led_pwm.duty(0)  # Iniciar apagado (duty 0)

# Potenciómetro en GPIO 34 (ADC1_CH6)
# Nota: Solo pines 34-39 pueden usarse como ADC
potenciometro = ADC(Pin(34))
potenciometro.atten(ADC.ATTN_11DB)  # Rango 0-3.3V (atenución completa)

# Constantes
ADC_RESOLUCION = 4096  # ADC de 12 bits (0-4095)
BRILLO_MAX = 1023  # Duty cycle máximo (10 bits)

# Mensaje inicial
print("=" * 50)
print("Ejemplo: Potenciómetro + LED")
print("GPIO 2 -> LED (PWM), GPIO 34 -> Potenciómetro (ADC)")
print("Gira el potenciómetro para cambiar el brillo")
print("=" * 50)


def leer_potenciometro():
    """
    Lee el valor del potenciómetro

    Returns:
        int: Valor de 0 a 4095
    """
    return potenciometro.read()


def valor_a_brillo(valor_adc):
    """
    Convierte el valor del ADC al brillo del LED

    Args:
        valor_adc: Valor del potenciómetro (0-4095)

    Returns:
        int: Brillo para PWM (0-1023)
    """
    return int((valor_adc / ADC_RESOLUCION) * BRILLO_MAX)


# Bucle principal
while True:
    # Leer valor del potenciómetro
    valor = leer_potenciometro()

    # Convertir a brillo
    brillo = valor_a_brillo(valor)

    # Aplicar al LED
    led_pwm.duty(brillo)

    # Calcular porcentaje
    porcentaje = int((brillo / BRILLO_MAX) * 100)

    # Mostrar información
    barras = "█" * int(porcentaje / 5)
    print(f"ADC: {valor:4d} | Brillo: {porcentaje:3d}% | {barras}")

    # Pequeña pausa
    time.sleep(0.1)
