"""
Joystick Analógico - Controlando con Dos Dedos
=============================================

¿QUÉS ES ESTO?
Un joystick analógico es como el control de tus videojuegos favoritos: te permite
medir exactamente en qué posición está la palanca en dos direcciones (izquierda-derecha y arriba-abajo). Es perfecto para controlar robots, crear juegos o hacer interfaces interactivas.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes: Joystick analógico de 2 ejes (tipo KY-023 o similar)

📌 CONEXIONES FÍSICAS:
─────────────────────────────────────────────────────────
   GPIO 26 (Pico) ────► VRX (eje horizontal / X)
   GPIO 27 (Pico) ────► VRY (eje vertical / Y)
   VCC (3.3V Pico) ────► VCC
   GND (Pico) ─────────► GND

   ⚠️ NOTA: GPIO 26 y 27 son pines ADC del Pico (conversor analógico)

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

from machine import Pin, ADC
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE PINES
# ─────────────────────────────────────────────────────────────────────────

# El joystick usa dos pines ADC (lectura analógica)
# GPIO 26 → Eje horizontal (X)
eje_x = ADC(Pin(26))

# GPIO 27 → Eje vertical (Y)
eje_y = ADC(Pin(27))

# Valores de referencia
CENTRO = 2048  # Valor cuando el joystick está en el medio
# (ADC de 12 bits: 0 a 4095, centro = 2048)
UMBRAL = 500  # Cuánta diferencia para considerar "movimiento"
# Si está a ±500 del centro, consideramos que se mueve


def leer_joystick():
    """
    Lee la posición actual del joystick

    Returns:
        tuple: (valor_x, valor_y) ambos de 0 a 4095
    """
    x = eje_x.read()
    y = eje_y.read()
    return x, y


def obtener_direccion(x, y):
    """
    Determina la dirección based en la posición

    Compara la posición actual con el centro y decide dirección.
    """
    # Calcular qué tan lejos está del centro
    dx = x - CENTRO
    dy = y - CENTRO

    # Si está muy cerca del centro → "en reposo"
    if abs(dx) < UMBRAL and abs(dy) < UMBRAL:
        return "🎯 CENTRO"

    # Construir la dirección basada en los ejes
    direccion = ""

    # Eje Y (arriba/abajo) - NOTA: muchos joysticks están invertidos
    if dy < -UMBRAL:
        direccion += "⬆️ ARRIBA "
    elif dy > UMBRAL:
        direccion += "⬇️ ABAJO "

    # Eje X (izquierda/derecha)
    if dx < -UMBRAL:
        direccion += "⬅️ IZQUIERDA"
    elif dx > UMBRAL:
        direccion += "➡️ DERECHA"

    return direccion.strip()


# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("🕹️ INICIANDO: Joystick Analógico")
print("   GPIO 26 → Eje X (horizontal)")
print("   GPIO 27 → Eje Y (vertical)")
print("   ¡Mueve el joystick para ver los valores!")
print("=" * 50)

# Loop principal
while True:
    # Leer posición actual
    x, y = leer_joystick()
    direccion = obtener_direccion(x, y)

    # Mostrar valores crudos
    print(f"📊 X: {x:4d} | Y: {y:4d} → {direccion}")

    # Representación visual del Eje X (horizontal)
    if x < CENTRO - UMBRAL:
        # Movido a la izquierda
        distancia = int((CENTRO - x) / 200) + 1
        x_barra = "█" * distancia + "░" * (11 - distancia)
    elif x > CENTRO + UMBRAL:
        # Movido a la derecha
        distancia = int((x - CENTRO) / 200) + 1
        x_barra = "░" * (11 - distancia) + "█" * distancia
    else:
        # En el centro
        x_barra = "░░░░░░░░░░░"

    # Representación visual del Eje Y (vertical)
    if y < CENTRO - UMBRAL:
        distancia = int((CENTRO - y) / 200) + 1
        y_barra = "█" * distancia + "░" * (11 - distancia)
    elif y > CENTRO + UMBRAL:
        distancia = int((y - CENTRO) / 200) + 1
        y_barra = "░" * (11 - distancia) + "█" * distancia
    else:
        y_barra = "░░░░░░░░░░░"

    print(f"   X: {x_barra}")
    print(f"   Y: {y_barra}")
    print("-" * 40)

    # Pausa pequeña (100ms) para no saturar la consola
    time.sleep(0.1)
