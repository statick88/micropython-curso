"""
Control de LED RGB - ESP32 con MicroPython
==========================================
Hardware: ESP32 DevKit V1
Componentes: 1 LED RGB (ánodo común) y 3 resistores de 220Ω
Conexionado: GPIO 25 -> Rojo, GPIO 26 -> Verde, GPIO 27 -> Azul
Lenguaje: MicroPython
Lógica: Secuencia de colores que cambia cada 500ms
"""

from machine import Pin
import time

# Configuración de pines como salida
# LED RGB de ánodo común: nivel bajo = LED encendido
# Usamos GPIO 25, 26, 27 (pines disponibles en ESP32 DevKit)
rojo = Pin(25, Pin.OUT)
verde = Pin(26, Pin.OUT)
azul = Pin(27, Pin.OUT)


# Función para establecer color
def establecer_color(r, v, a):
    """
    Establece el color del LED RGB

    Args:
        r: Rojo (True = activo)
        v: Verde (True = activo)
        a: Azul (True = activo)

    Nota: LED de ánodo común -> valor invertido
    """
    rojo.value(not r)
    verde.value(not v)
    azul.value(not a)


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

nombres = ["ROJO", "VERDE", "AZUL", "AMARILLO", "MAGENTA", "CIAN", "BLANCO", "APAGADO"]

# Mensaje inicial
print("=" * 50)
print("Ejemplo: LED RGB con ESP32")
print("Pines: GPIO 25 (R), GPIO 26 (G), GPIO 27 (B)")
print("=" * 50)

# Bucle infinito con secuencia de colores
indice = 0
while True:
    # Obtener el color actual
    color = colores[indice]
    establecer_color(*color)

    # Mensaje por consola
    print(f"Color: {nombres[indice]}")

    # Esperar 500ms antes del siguiente color
    time.sleep(0.5)

    # Avanzar al siguiente color (cíclico)
    indice = (indice + 1) % len(colores)
