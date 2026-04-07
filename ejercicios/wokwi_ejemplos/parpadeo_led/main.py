"""
Parpadeo de LED - Ejemplo Introductorio para Wokwi
=================================================
Hardware: Raspberry Pi Pico con MicroPython
Componentes: 1 LED rojo y 1 resistor de 220Ω
Conexionado: El pin GPIO 15 del Pico está conectado al ánodo del LED
            El cátodo del LED está conectado a GND mediante resistencia
Lenguaje: MicroPython
"""

# Importamos las librerías necesarias
from machine import Pin
import time

# Configuración de los Pines
# Definimos el pin GPIO 15 como salida para controlar el LED
led = Pin(15, Pin.OUT)

# Mensaje inicial por consola serie
print("Iniciando ejemplo de parpadeo de LED...")
print("El LED parpadeará cada 1 segundo")

# Bucle infinito que alterna el estado del LED cada segundo
while True:
    led.value(1)  # Encender el LED (nivel alto = 3.3V)
    print("LED ENCENDIDO")  # Mensaje de debug por serie
    time.sleep(1)  # Esperar 1 segundo (LED encendido)

    led.value(0)  # Apagar el LED (nivel bajo = 0V)
    print("LED APAGADO")  # Mensaje de debug por serie
    time.sleep(1)  # Esperar 1 segundo (LED apagado)
