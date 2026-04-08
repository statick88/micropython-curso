"""
Encoder Rotativo KY-040 - Botón que Gira Infinito
==============================================

¿QUÉS ES ESTO?
Es como una perilla de volumen que puede girar sin límites (360°+).
A diferencia de un potenciómetro que tiene un máximo y mínimo, el encoder
puede girar constantemente (como las perillas de los sintetizadores).

Se usa en:
• Perillas de volumen (equipos de música)
• Menús de navegación (como en microondas)
• Controles de máquinas industriales
• Ruedas de ratón para scrolling
• Ajustes de temperatura en hornos

📚 CÓMO FUNCIONA:
─────────────────────────────────────────────────────────────────────────
El encoder tiene dos contactos (CLK y DT) que se tocan y separan según gira.

Imagina dos amigos dandose la mano:
• Cuando gira a la DERECHA: CLK toca DT primero, luego se separan
• Cuando gira a la IZQUIERDA: DT toca CLK primero, luego se separan

Esta secuencia de "tocarse" crea una señal cuadrada:

   Giro DERECHA (CW):      Giro IZQUIERDA (CCW):
     CLK ┌─┐┌─┐              CLK ┌─┐┌─┐
         │ ││ │                  │ ││ │
     ────┘ └─┘└──          ────┘ └─┘└──
     DT  ┌─┐┌─┐             DT  ┌─┐┌─┐
         │ ││ │                  │ ││ │
     ────┘ └─┘└──          ────┘ └─┘└──

Detectando CUÁL señal cambia PRIMERO, sabemos la dirección.

También tiene un botón (SW) en el centro que se presiona como cualquier
botón normal cuando empujas la perilla.

📚 TIPOS DE ENCODERS:
─────────────────────────────────────────────────────────────────────────
• Incremental (el más común): cuenta pulsos, no sabe posición absoluta
• Absoluto: sabe su posición exacta siempre (más caro, más complejo)

Nosotros usamos uno incremental (KY-040).

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes: Encoder rotativo KY-040

📌 CONEXIONES FÍSICAS:
─────────────────────────────────────────────────────────
   El encoder tiene 5 pines:
     CLK (Clock) → GPIO 15 (señal A)
     DT (Data) → GPIO 14 (señal B)
     SW (Switch) → GPIO 13 (botón central)
     VCC → 3.3V (Pico)
     GND → GND (Pico)

   Los pines CLK y DT necesitan resistencias PULL-DOWN (o las usamos
   integradas del microcontrolador).

   El botón SW usa PULL-UP porque cuando no está presionado, está en alto.

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

# CLK (Clock/Señal A): Detecta pulsos de rotación
# Usamos PULL-DOWN para que esté en bajo cuando no hay señal
clk = Pin(15, Pin.IN, Pin.PULL_DOWN)

# DT (Data/Señal B): Detecta la dirección
# También con PULL-DOWN
dt = Pin(14, Pin.IN, Pin.PULL_DOWN)

# SW (Switch): El botón en el centro de la perilla
# PULL-UP porque cuando no se presiona, está en alto (3.3V)
sw = Pin(13, Pin.IN, Pin.PULL_UP)

# Variables de estado
contador = 0  # Cuenta los pasos del encoder
estado_clk = 0  # Estado anterior del CLK
estado_dt = 0  # Estado anterior del DT
ultimo_estado_sw = 1  # Estado anterior del botón


def obtener_direccion():
    """
    Detecta si hay rotación y en qué dirección

    Returns:
        1 = giró a la derecha (clockwise)
        -1 = giró a la izquierda (counter-clockwise)
        0 = sin cambio
    """
    global estado_clk, estado_dt

    # Leer estados actuales
    nuevo_clk = clk.value()
    nuevo_dt = dt.value()

    # Detectar cambio en la señal CLK
    if nuevo_clk != estado_clk:
        # Actualizar estado
        estado_clk = nuevo_clk

        # Solo nos importa cuando CLK pasa de bajo a alto (flanco-subida)
        if nuevo_clk == 1:
            # Determinar dirección mirando el estado de DT
            # Si DT está en bajo → giró a la derecha
            # Si DT está en alto → giró a la izquierda
            if nuevo_dt == 0:
                return 1  # ↻ Derecha (CW)
            else:
                return -1  # ↺ Izquierda (CCW)

    return 0  # Sin cambio


# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("🎚️ INICIANDO: Encoder Rotativo KY-040")
print("   GPIO 15 → CLK (señal A)")
print("   GPIO 14 → DT (señal B)")
print("   GPIO 13 → SW (botón)")
print("   ¡Gira la perilla para ver el contador!")
print("=" * 50)

while True:
    # 1. Verificar si hay rotación
    direccion = obtener_direccion()

    if direccion != 0:
        # Actualizar contador
        contador += direccion

        # Mostrar información
        if direccion > 0:
            print(f"↻ Giro DERECHA → Contador: {contador}")
        else:
            print(f"↺ Giro IZQUIERDA → Contador: {contador}")

    # 2. Verificar botón (detectar presión)
    estado_actual_sw = sw.value()

    # Detectar flanco de caída (botón presionado)
    if estado_actual_sw == 0 and ultimo_estado_sw == 1:
        print("🔘 ¡BOTÓN PRESIONADO! → Reiniciando contador")
        contador = 0
        print("   🔢 Contador = 0")

    # Recordar estado para próxima iteración
    ultimo_estado_sw = estado_actual_sw

    # Pausa pequeña para no saturar el CPU
    time.sleep(0.001)
