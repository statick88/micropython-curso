"""
LED RGB - Todos los Colores con un Solo LED
========================================

¿QUÉS ES ESTO?
El LED RGB es como tener tres luces de colores (rojo, verde y azul) en un
solo componente. Al brillar con diferentes intensidades, podemos crear
cualquier color del arcoíris, igual que en tu televisor o smartphone.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes:
   • 1 LED RGB (ánodo común)
   • 3 resistores de 220Ω (uno por cada color)

📌 CONEXIONES FÍSICAS (4 cables + 3 resistores):
─────────────────────────────────────────────────────────
   El LED RGB tiene 4 patitas:
     1. ÁNODO (la más larga) → se conecta a 3.3V a través de resistores
     2. R (Rojo) → GPIO 15
     3. G (Verde) → GPIO 14
     4. B (Azul) → GPIO 13

   Cada color necesita su propio resistor de 220Ω para no quemarse:

   GPIO 15 ────► R (con resistor 220Ω) ──┐
   GPIO 14 ────► G (con resistor 220Ω) ──┼──► ÁNODO ──► 3.3V
   GPIO 13 ────► B (con resistor 220Ω) ──┘

   ¿Por qué ánodo común? Porque cuando queremos que un color brille,
  ponemos su pin en BAJO (0V), creando diferencia de potencial.

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

from machine import Pin
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE PINES
# ─────────────────────────────────────────────────────────────────────────
# Configuramos 3 pines como SALIDA, uno para cada color
# Como usamos ánodo común: 1 = apagado, 0 = encendido
rojo = Pin(15, Pin.OUT)  # Pin del color rojo
verde = Pin(14, Pin.OUT)  # Pin del color verde
azul = Pin(13, Pin.OUT)  # Pin del color azul


def apagar_todos():
    """
    Apaga todos los colores del LED RGB

    Con ánodo común, necesitamos poner todos los pines en ALTO (1)
    para que no haya diferencia de voltaje y no pase corriente.
    """
    rojo.value(1)
    verde.value(1)
    azul.value(1)


def establecer_color(encender_rojo, encender_verde, encender_azul):
    """
    Enciende los colores que quieras del LED RGB

    Args:
        rojo: True para activar rojo, False para apagar
        verde: True para activar verde, False para apagar
        azul: True para activar azul, False para apagar

    Ejemplo: establecer_color(True, False, True) = Magenta
    """
    # Con ánodo común, invertimos la lógica:
    # True (encender) → poner en BAJO (0)
    # False (apagar) → poner en ALTO (1)
    rojo.value(not encender_rojo)
    verde.value(not encender_verde)
    azul.value(not encender_azul)


# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL - SECUENCIA DE COLORES
# ═══════════════════════════════════════════════════════════════════════════

# Definimos los colores que mostraremos
# Formato: (rojo, verde, azul) → True = encender ese color
colores = [
    (True, False, False),  # 🔴 ROJO
    (False, True, False),  # 🟢 VERDE
    (False, False, True),  # 🔵 AZUL
    (True, True, False),  # 🟡 AMARILLO
    (True, False, True),  # 🩽 MAGENTA
    (False, True, True),  # 🔷 CIAN
    (True, True, True),  # ⚪ BLANCO
    (False, False, False),  # ⚫ APAGADO
]

# Nombres para mostrar en consola
nombres_colores = [
    "ROJO",
    "VERDE",
    "AZUL",
    "AMARILLO",
    "MAGENTA",
    "CIAN",
    "BLANCO",
    "APAGADO",
]

print("🌈 INICIANDO: LED RGB")
print("   Secuencia de colores - cada 500ms")
print("-" * 40)

indice = 0
while True:
    # Obtener el color actual de la lista
    color_actual = colores[indice]

    # Aplicar el color al LED
    establecer_color(*color_actual)

    # Mostrar qué color está activo
    print(f"🎨 Color: {nombres_colores[indice]}")

    # Esperar 500ms antes de cambiar
    time.sleep(0.5)

    # Avanzar al siguiente color (y volver al inicio si llega al final)
    indice = (indice + 1) % len(colores)
