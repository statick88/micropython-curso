"""
Sensor PIR (Movimiento) - Raspberry Pi Pico
===========================================
Hardware: Raspberry Pi Pico
Componentes: 1 LED, 1 resistor, 1 sensor PIR HC-SR501
Conexionado: GPIO 15 -> LED, GPIO 16 -> PIR (señal)
Lenguaje: MicroPython
Lógica: Detecta movimiento y enciende LED
"""

from machine import Pin
import time

# Configuración de pines
# LED indicador
led = Pin(15, Pin.OUT)
led.value(0)

# Sensor PIR en GPIO 16
# El PIR devuelve 1 cuando detecta movimiento
pir = Pin(16, Pin.IN)

# Contador de detecciones
detecciones = 0
ultimo_estado = 0

# Mensaje inicial
print("=" * 50)
print("Sensor de Movimiento PIR")
print("GPIO 15 -> LED, GPIO 16 -> PIR")
print("Mueve tu mano frente al sensor!")
print("=" * 50)

# Bucle principal
while True:
    # Leer estado del PIR
    estado = pir.value()

    # Detectar flanco de subida (inicio de movimiento)
    if estado == 1 and ultimo_estado == 0:
        led.value(1)  # Encender LED
        detecciones += 1
        print(f"🚨 MOVIMIENTO DETECTADO! (#{detecciones})")
        print("   LED ENCENDIDO")

    # Detectar flanco de bajaa (fin de movimiento)
    elif estado == 0 and ultimo_estado == 1:
        led.value(0)  # Apagar LED
        print("✅ Movimiento terminado")
        print("   LED APAGADO")
        print("-" * 40)

    # Actualizar estado anterior
    ultimo_estado = estado

    # Pequeña pausa
    time.sleep(0.1)
