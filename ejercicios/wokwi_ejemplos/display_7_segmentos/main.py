"""
Contador con Display de 7 Segmentos - Ejemplo de Salida Numérica
=============================================================
Hardware: Raspberry Pi Pico con MicroPython
Componentes: 1 display de 7 segmentos (cátodo común)
Conexionado: GPIO 10-17 para los segmentos a-g y punto decimal
Lenguaje: MicroPython
Lógica: Cuenta de 0 a 9 con actualización cada segundo
"""

from machine import Pin
import time

# Definición de pines para cada segmento del display
# Display de 7 segmentos: a, b, c, d, e, f, g
segmentos = [
    Pin(10, Pin.OUT),  # Segmento a
    Pin(11, Pin.OUT),  # Segmento b
    Pin(12, Pin.OUT),  # Segmento c
    Pin(13, Pin.OUT),  # Segmento d
    Pin(14, Pin.OUT),  # Segmento e
    Pin(15, Pin.OUT),  # Segmento f
    Pin(16, Pin.OUT),  # Segmento g
]

# Mapeo de números a segmentos (True = segmento activo)
# Formato: [a, b, c, d, e, f, g]
NUMEROS = {
    0: [True, True, True, True, True, True, False],
    1: [False, True, True, False, False, False, False],
    2: [True, True, False, True, True, False, True],
    3: [True, True, True, True, False, False, True],
    4: [False, True, True, False, False, True, True],
    5: [True, False, True, True, False, True, True],
    6: [True, False, True, True, True, True, True],
    7: [True, True, True, False, False, False, False],
    8: [True, True, True, True, True, True, True],
    9: [True, True, True, True, False, True, True],
}


def mostrar_numero(numero):
    """
    Muestra un número en el display de 7 segmentos

    Args:
        numero: Entero de 0 a 9
    """
    if numero not in NUMEROS:
        print(f"Error: Número {numero} no válido")
        return

    valores = NUMEROS[numero]
    for i, segmento in enumerate(segmentos):
        segmento.value(valores[i])


def mostrar_letra(letra):
    """
    Muestra una letra en el display (ejemplo básico)

    Args:
        letra: String con la letra a mostrar
    """
    # Letras simples que pueden mostrarse
    LETRAS = {
        "A": [True, True, True, False, True, True, True],  # Similar a 9
        "E": [True, False, False, True, True, True, True],  # Similar a 3
        "F": [True, False, False, False, True, True, True],  # Similar a 1
        "L": [False, False, False, True, True, True, False],  # Similar a 1
        "S": [True, False, True, True, False, True, True],  # Similar a 5
    }

    if letra.upper() not in LETRAS:
        print(f"Error: Letra {letra} no implementada")
        return

    valores = LETRAS[letra.upper()]
    for i, segmento in enumerate(segmentos):
        segmento.value(valores[i])


# Mensaje inicial
print("Iniciando contador con display de 7 segmentos...")
print("Contando de 0 a 9")

# Contador principal
contador = 0
while True:
    # Mostrar el número actual
    mostrar_numero(contador)
    print(f"Mostrando: {contador}")

    # Esperar 1 segundo
    time.sleep(1)

    # Incrementar el contador (0-9 cíclico)
    contador = (contador + 1) % 10
