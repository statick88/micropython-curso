"""
Parpadeo de LED - ESP32 con MicroPython
=======================================
Hardware: ESP32 DevKit V1
Componentes: 1 LED rojo y 1 resistor de 220Ω
Conexionado: Pin GPIO 2 del ESP32 conectado al ánodo del LED
            El cátodo conectado a GND mediante resistencia
Lenguaje: MicroPython
"""

# Importamos las librerías necesarias
from machine import Pin
import time

# Configuración del Pines
# Definimos el pin GPIO 2 como salida para controlar el LED
# Nota: GPIO 2 es el LED azul integrado en la mayoría de ESP32
led = Pin(2, Pin.OUT)

# Mensaje inicial por consola serie
print("=" * 50)
print("Ejemplo: Parpadeo de LED con ESP32")
print("Pin GPIO 2 configurado como salida")
print("=" * 50)

# Bucle infinito que alterna el estado del LED cada segundo
contador = 0
while True:
    led.value(1)  # Encender el LED (nivel alto = 3.3V)
    print(f"[{contador}] LED ENCENDIDO")
    time.sleep(1)  # Esperar 1 segundo

    led.value(0)  # Apagar el LED (nivel bajo = 0V)
    print(f"[{contador}] LED APAGADO")
    time.sleep(1)  # Esperar 1 segundo

    contador += 1
