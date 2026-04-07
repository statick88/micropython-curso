"""
Botón con LED - ESP32 con MicroPython
====================================
Hardware: ESP32 DevKit V1
Componentes: 1 LED, 1 resistor 220Ω, 1 botón pulsador
Conexionado: GPIO 2 -> LED, GPIO 4 -> Botón
Lenguaje: MicroPython
Lógica: El LED se enciende mientras se presiona el botón
"""

from machine import Pin
import time

# Configuración de pines
# LED en GPIO 2 como salida
led = Pin(2, Pin.OUT)
led.value(0)  # Iniciar apagado

# Botón en GPIO 4 como entrada con pull-down interno
# Pull-down: cuando no se presiona, el pin lee 0 (bajo)
boton = Pin(4, Pin.IN, Pin.PULL_DOWN)

# Contador de pulsaciones
pulsaciones = 0

# Mensaje inicial
print("=" * 50)
print("Ejemplo: Botón con LED")
print("GPIO 2 -> LED, GPIO 4 -> Botón")
print("Presiona el botón para encender el LED")
print("=" * 50)

# Bucle principal
while True:
    # Leer estado del botón
    estado_boton = boton.value()

    if estado_boton == 1:  # Botón presionado (nivel alto)
        led.value(1)  # Encender LED
        pulsaciones += 1
        print(f"🔘 Botón PRESIONADO (pulsación #{pulsaciones})")
    else:  # Botón no presionado (nivel bajo)
        led.value(0)  # Apagar LED

    # Pequeña pausa para evitar rebotes
    time.sleep(0.05)
