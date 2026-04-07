"""
Sensor de Gas MQ-2 - ESP32
==========================
Hardware: ESP32 DevKit V1
Componentes: 1 LED, 1 resistor, 1 sensor de gas MQ-2
Conexionado: GPIO 2 -> LED, GPIO 34 -> Sensor Gas (ADC)
Lenguaje: MicroPython
Lógica: Detecta gases inflamables (propano, metano, etc.)
"""

from machine import Pin, ADC
import time

# Configuración de pines
# LED indicador de alarma
led = Pin(2, Pin.OUT)
led.value(0)

# Sensor MQ-2 en GPIO 34 (ADC)
# Nota: Solo pines 34-39 pueden usarse como ADC
sensor_gas = ADC(Pin(34))
sensor_gas.atten(ADC.ATTN_11DB)  # Rango completo 0-3.3V

# Constantes
# Umbrales típicos para MQ-2 (ajustar según necesidad)
UMBRAL_SEGURO = 500
UMBRAL_PELIGRO = 1500
UMBRAL_DANGER = 3000


def leer_gas():
    """Lee el valor del sensor de gas"""
    # Promedio de varias lecturas para mayor estabilidad
    total = 0
    for _ in range(10):
        total += sensor_gas.read()
        time.sleep(0.01)
    return total // 10


def obtener_nivel_gas(valor):
    """Clasificación del nivel de gas detectado"""
    if valor < UMBRAL_SEGURO:
        return "✅ SEGURO"
    elif valor < UMBRAL_PELIGRO:
        return "⚠️ ADVERTENCIA"
    elif valor < UMBRAL_DANGER:
        return "🚨 PELIGRO!"
    else:
        return "💀 PELIGRO CRÍTICO!"


# Mensaje inicial
print("=" * 50)
print("Sensor de Gas MQ-2 - ESP32")
print("GPIO 2 -> LED, GPIO 34 -> MQ-2 (ADC)")
print("Detecta: Propano, Metano, Butano, Humo")
print("=" * 50)

# Bucle principal
while True:
    valor = leer_gas()
    nivel = obtener_nivel_gas(valor)

    # Activar alarma según el nivel
    if valor >= UMBRAL_PELIGRO:
        led.value(1)  # LED de alarma
        alarma = "🚨 ALARMA"
    else:
        led.value(0)
        alarma = "⚫ OK"

    # Mostrar información
    print(f"Valor: {valor:4d} ppm | Estado: {nivel} | {alarma}")

    # Representación visual
    if valor < 1000:
        barras = "░" * int(valor / 50) + "█" * 3
    else:
        barras = "█" * 20

    print(f"  Nivel: {barras}")
    print("-" * 40)

    time.sleep(0.5)
