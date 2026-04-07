"""
Teclado Matricial 4x4 - Raspberry Pi Pico
===========================================
Hardware: Raspberry Pi Pico
Componentes: 1 Teclado matricial 4x4
Conexionado: Filas GPIO 8-11, Columnas GPIO 12-15
Lenguaje: MicroPython
Lógica: Lee teclas presionadas del teclado
"""

from machine import Pin
import time

# Configuración del teclado 4x4
filas = [Pin(8, Pin.OUT), Pin(9, Pin.OUT), Pin(10, Pin.OUT), Pin(11, Pin.OUT)]

columnas = [
    Pin(12, Pin.IN, Pin.PULL_DOWN),
    Pin(13, Pin.IN, Pin.PULL_DOWN),
    Pin(14, Pin.IN, Pin.PULL_DOWN),
    Pin(15, Pin.IN, Pin.PULL_DOWN),
]

# Mapeo del teclado
TECLADO = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"],
]


def escanear():
    """Escanea el teclado"""
    for i, fila in enumerate(filas):
        fila.value(1)
        for j, col in enumerate(columnas):
            if col.value() == 1:
                fila.value(0)
                return TECLADO[i][j]
        fila.value(0)
    return None


# Inicializar
for f in filas:
    f.value(0)

print("=" * 50)
print("Teclado Matricial 4x4")
print("Filas: GPIO 8-11, Columnas: 12-15")
print("Presiona una tecla...")
print("=" * 50)

ultima = None

while True:
    tecla = escanear()
    if tecla and tecla != ultima:
        print(f"🔢 Tecla: {tecla}")
        ultima = tecla
    elif not tecla:
        ultima = None
    time.sleep(0.05)
