"""
Control de LED RGB - Ejemplo de Salidas Múltiples
===============================================
Hardware: Raspberry Pi Pico con MicroPython
Componentes: 1 LED RGB (ánodo común) y 3 resistores de 220Ω
Conexionado: GPIO 15 -> Rojo, GPIO 14 -> Verde, GPIO 13 -> Azul
Lenguaje: MicroPython
Lógica: Secuencia de colores que cambia cada 500ms
"""

from machine import Pin
import time

# Configuración de pines como salida
# LED RGB de ánodo común: nivel bajo = LED encendido
rojo = Pin(15, Pin.OUT)
verde = Pin(14, Pin.OUT)
azul = Pin(13, Pin.OUT)


# Función para apagar todos los LEDs
def apagar_todos():
    """Apaga el LED RGB completamente"""
    rojo.value(1)
    verde.value(1)
    azul.value(1)


# Función para establecer color
def establecer_color(r, v, a):
    """
    Establece el color del LED RGB

    Args:
        r: Rojo (True = activo)
        v: Verde (True = activo)
        a: Azul (True = activo)
    """
    rojo.value(not r)  # Invertido porque es ánodo común
    verde.value(not v)
    azul.value(not a)


# Mensaje inicial
print("Iniciando ejemplo de LED RGB...")
print("Secuencia de colores iniciada")

# Secuencia de colores predefinidos
colores = [
    (True, False, False),  # Rojo
    (False, True, False),  # Verde
    (False, False, True),  # Azul
    (True, True, False),  # Amarillo
    (True, False, True),  # Magenta
    (False, True, True),  # Cian
    (True, True, True),  # Blanco
    (False, False, False),  # Apagado
]

# Bucle infinito con secuencia de colores
indice = 0
while True:
    # Obtener el color actual
    color = colores[indice]
    establecer_color(*color)

    # Mensaje por consola
    nombre_color = [
        "ROJO",
        "VERDE",
        "AZUL",
        "AMARILLO",
        "MAGENTA",
        "CIAN",
        "BLANCO",
        "APAGADO",
    ][indice]
    print(f"Color: {nombre_color}")

    # Esperar 500ms antes del siguiente color
    time.sleep(0.5)

    # Avanzar al siguiente color (cíclico)
    indice = (indice + 1) % len(colores)
