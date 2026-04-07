"""
Joystick Analógico - Raspberry Pi Pico
=======================================
Hardware: Raspberry Pi Pico
Componentes: 1 Joystick analógico de 2 ejes
Conexionado: GPIO 26 -> Eje X, GPIO 27 -> Eje Y
Lenguaje: MicroPython
Lógica: Lee la posición del joystick
"""

from machine import Pin, ADC
import time

# Configuración del joystick
# Eje X en GPIO 26 (ADC)
eje_x = ADC(Pin(26))
# Eje Y en GPIO 27 (ADC)
eje_y = ADC(Pin(27))

# Valores del centro (aproximadamente 2048 para ADC de 12 bits)
CENTRO = 2048
UMBRAL = 500  # Para considerar que hay movimiento


def leer_joystick():
    """Lee la posición del joystick"""
    x = eje_x.read()
    y = eje_y.read()
    return x, y


def obtener_direccion(x, y):
    """Determina la dirección based en la posición"""
    dx = x - CENTRO
    dy = y - CENTRO

    # Verificar si hay movimiento significativo
    if abs(dx) < UMBRAL and abs(dy) < UMBRAL:
        return "CENTRO"

    # Determinar dirección
    direccion = ""

    if dy < -UMBRAL:
        direccion += "ARRIBA "
    elif dy > UMBRAL:
        direccion += "ABAJO "

    if dx < -UMBRAL:
        direccion += "IZQUIERDA"
    elif dx > UMBRAL:
        direccion += "DERECHA"

    return direccion.strip()


# Mensaje inicial
print("=" * 50)
print("Joystick Analógico")
print("GPIO 26 -> Eje X, GPIO 27 -> Eje Y")
print("Mueve el joystick...")
print("=" * 50)

# Bucle principal
while True:
    x, y = leer_joystick()
    direccion = obtener_direccion(x, y)

    # Mostrar valores
    print(f"X: {x:4d} | Y: {y:4d} | Dirección: {direccion}")

    # Representación visual
    # Eje X: izquierda-derecha
    if x < CENTRO - UMBRAL:
        x_barra = "█" * int((CENTRO - x) / 200) + "░" * 10
    elif x > CENTRO + UMBRAL:
        x_barra = "░" * 10 + "█" * int((x - CENTRO) / 200)
    else:
        x_barra = "░░░░░░░░░░"

    # Eje Y: arriba-abajo
    if y < CENTRO - UMBRAL:
        y_barra = "█" * int((CENTRO - y) / 200)
    elif y > CENTRO + UMBRAL:
        y_barra = "░" * 10 + "█" * int((y - CENTRO) / 200)
    else:
        y_barra = "░░░░░░░░░░"

    print(f"  X: {x_barra}")
    print(f"  Y: {y_barra}")
    print("-" * 40)

    time.sleep(0.1)
