"""
Encoder Rotativo KY-040 - Raspberry Pi Pico
=============================================
Hardware: Raspberry Pi Pico
Componentes: 1 Encoder rotativo KY-040
Conexionado: GPIO 15 -> CLK, GPIO 14 -> DT
Lenguaje: MicroPython
Lógica: Detecta rotación y pulsaciones del encoder
"""

from machine import Pin
import time

# Configuración del encoder
# CLK (Clock) - señal de rotación
clk = Pin(15, Pin.IN, Pin.PULL_DOWN)
# DT (Data) - dirección de rotación
dt = Pin(14, Pin.IN, Pin.PULL_DOWN)
# SW (Switch) - botón central
sw = Pin(13, Pin.IN, Pin.PULL_UP)

# Variables de estado
contador = 0
estado_clk = 0
estado_dt = 0
ultimo_estado_sw = 1


def obtener_direccion():
    """
    Obtiene la dirección de rotación

    Returns:
        int: 1 = clockwise, -1 = counter-clockwise, 0 = sin cambio
    """
    global estado_clk, estado_dt

    nuevo_clk = clk.value()
    nuevo_dt = dt.value()

    # Detectar cambio en CLK
    if nuevo_clk != estado_clk:
        estado_clk = nuevo_clk
        # Si CLK cambió a alto
        if nuevo_clk == 1:
            # Determinar dirección basado en DT
            if nuevo_dt == 0:
                return 1  # clockwise
            else:
                return -1  # counter-clockwise

    return 0


# Mensaje inicial
print("=" * 50)
print("Encoder Rotativo KY-040")
print("GPIO 15 -> CLK, GPIO 14 -> DT, GPIO 13 -> SW")
print("Gira el encoder para cambiar el contador")
print("=" * 50)

# Bucle principal
while True:
    # Verificar rotación
    direccion = obtener_direccion()

    if direccion != 0:
        contador += direccion
        sentido = "↻ DERECHA" if direccion > 0 else "↺ IZQUIERDA"
        print(f"🔄 Giro: {sentido} | Contador: {contador}")

    # Verificar botón
    estado_sw = sw.value()
    if estado_sw == 0 and ultimo_estado_sw == 1:
        print("🔘 BOTÓN PRESIONADO! (Reiniciar contador)")
        contador = 0
        print("   Contador reiniciado a 0")

    ultimo_estado_sw = estado_sw

    # Pequeña pausa
    time.sleep(0.001)
