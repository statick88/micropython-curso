"""
Sensor de Efecto Hall - Raspberry Pi Pico
=========================================
Hardware: Raspberry Pi Pico
Componentes: 1 LED, 1 resistor, 1 imán, 1 sensor Hall
Conexionado: GPIO 15 -> LED, GPIO 16 -> Sensor Hall
Lenguaje: MicroPython
Lógica: Detecta campos magnéticos (iman cercano/lejano)
"""

from machine import Pin
import time

# Configuración de pines
# LED indicador
led = Pin(15, Pin.OUT)
led.value(0)

# Sensor Hall en GPIO 16
# Valor 1 = campo magnético detectado
# Valor 0 = sin campo magnético
hall = Pin(16, Pin.IN)

# Contador de detecciones
detecciones = 0
ultimo_estado = 0

# Mensaje inicial
print("=" * 50)
print("Sensor de Efecto Hall")
print("GPIO 15 -> LED, GPIO 16 -> Sensor Hall")
print("Acerca un imán para detectar el campo magnético")
print("=" * 50)

# Bucle principal
while True:
    # Leer estado del sensor
    estado = hall.value()

    # Detectar flanco de subida (iman detectado)
    if estado == 1 and ultimo_estado == 0:
        led.value(1)  # Encender LED
        detecciones += 1
        print(f"🧲 IMÁN DETECTADO! (#{detecciones})")
        print("   Campo magnético presente")
        print("   LED ENCENDIDO")

    # Detectar flanco de bajaa (iman retirado)
    elif estado == 0 and ultimo_estado == 1:
        led.value(0)  # Apagar LED
        print("✅ Imán retirado")
        print("   Campo magnético ausente")
        print("   LED APAGADO")
        print("-" * 40)

    # Actualizar estado anterior
    ultimo_estado = estado

    # Pequeña pausa
    time.sleep(0.1)
