"""
Display de 7 Segmentos - Los Números de los Relojes Digitales
==========================================================

¿QUÉS ES ESTO?
Un display de 7 segmentos es como tener siete pequeñas luces LED dispuestas en forma de "8" que podemos encender o apagar individualmente para formar números y algunas letras. Es la tecnología que ves en relojes digitales, microondas y calculadoras.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes: Display de 7 segmentos (cátodo común)

📌 CONEXIONES FÍSICAS:
─────────────────────────────────────────────────────────
   El display tiene 8 pines (7 segmentos + punto decimal):
     Pines GPIO del 10 al 16 → segmentos a, b, c, d, e, f, g
     (El punto decimal no lo usamos en este ejemplo)

     Cada segmento se conecta así:
       GPIO 10 → Segmento 'a' (con resistor 220Ω)
       GPIO 11 → Segmento 'b' (con resistor 220Ω)
       GPIO 12 → Segmento 'c' (con resistor 220Ω)
       GPIO 13 → Segmento 'd' (con resistor 220Ω)
       GPIO 14 → Segmento 'e' (con resistor 220Ω)
       GPIO 15 → Segmento 'f' (con resistor 220Ω)
       GPIO 16 → Segmento 'g' (con resistor 220Ω)

   ⚠️ IMPORTANTE: Cada segmento necesita un resistor de ~220Ω
   para no quemarse. Los LEDs del display son como cualquier LED.

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

# Crear un array de pines para los 7 segmentos
# Cada pin controla un segmento específico
segmentos = [
    Pin(10, Pin.OUT),  # a - segmento superior
    Pin(11, Pin.OUT),  # b - segmento superior derecho
    Pin(12, Pin.OUT),  # c - segmento inferior derecho
    Pin(13, Pin.OUT),  # d - segmento inferior
    Pin(14, Pin.OUT),  # e - segmento inferior izquierdo
    Pin(15, Pin.OUT),  # f - segmento superior izquierdo
    Pin(16, Pin.OUT),  # g - segmento central
]

# ═══════════════════════════════════════════════════════════════════════════
# MAPEO DE NÚMEROS A SEGMENTOS
# ═══════════════════════════════════════════════════════════════════════════

# Cada número se representa como una lista de 7 valores (True/False)
# que indican qué segmentos deben estar encendidos
# Orden: [a, b, c, d, e, f, g]

NUMEROS = {
    # Los segmentos que están en True se encienden
    0: [True, True, True, True, True, True, False],  # 0 = sin 'g'
    1: [False, True, True, False, False, False, False],  # 1 = solo b,c
    2: [True, True, False, True, True, False, True],  # 2
    3: [True, True, True, True, False, False, True],  # 3
    4: [False, True, True, False, False, True, True],  # 4
    5: [True, False, True, True, False, True, True],  # 5
    6: [True, False, True, True, True, True, True],  # 6
    7: [True, True, True, False, False, False, False],  # 7
    8: [True, True, True, True, True, True, True],  # 8 = todos
    9: [True, True, True, True, False, True, True],  # 9
}


def mostrar_numero(numero):
    """
    Muestra un número (0-9) en el display

    Args:
        numero: Entero entre 0 y 9

    ¿Cómo funciona?
    1. Busca el patrón de segmentos para ese número
    2. Para cada segmento, ponlo en ALTO (1) si debe estar encendido
       o en BAJO (0) si debe estar apagado
    """
    if numero not in NUMEROS:
        print(f"⚠️ Error: {numero} no es válido (0-9)")
        return

    # Obtener el patrón de segmentos
    patron = NUMEROS[numero]

    # Aplicar el patrón a cada pin
    for i, segmento in enumerate(segmentos):
        segmento.value(patron[i])


def mostrar_letra(letra):
    """
    Muestra una letra simple en el display

    No todas las letras son posibles, solo las que usan
    los segmentos disponibles.
    """
    # Algunas letras que funcionan:
    LETRAS = {
        "A": [True, True, True, False, True, True, True],  # como 9
        "E": [True, False, False, True, True, True, True],  # como 3
        "F": [True, False, False, False, True, True, True],  # como 1 sin c
        "L": [False, False, False, True, True, True, False],  # como 1 abajo
        "S": [True, False, True, True, False, True, True],  # como 5
    }

    if letra.upper() not in LETRAS:
        print(f"⚠️ Letra {letra} no disponible")
        return

    patron = LETRAS[letra.upper()]
    for i, segmento in enumerate(segmentos):
        segmento.value(patron[i])


# ═══════════════════════════════════════════════════════════════════════════
# PROGRAMA PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("🔢 INICIANDO: Display de 7 Segmentos")
print("   Pines GPIO 10-16 → Segmentos a-g")
print("   Contador de 0 a 9")
print("=" * 50)

contador = 0

# Loop principal - contar eternamente
while True:
    # Mostrar el número actual
    mostrar_numero(contador)
    print(f"📊 Mostrando número: {contador}")

    # Esperar 1 segundo antes del siguiente
    time.sleep(1)

    # Incrementar (cuando llegue a 10, vuelve a 0)
    contador = (contador + 1) % 10
