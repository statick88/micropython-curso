"""
Contador con Botones - Interactuando con tu Microcontrolador
============================================================

¿QUÉS ES ESTO?
Vamos a crear un contador digital. Cuando presione un botón, el número
aumenta. Cuando presione otro botón, el contador vuelve a cero.

Este es un proyecto fundamental porque enseña:
• 📥 Cómo leer botones (entradas digitales)
• 🔄 Cómo detectar cuando se presiona un botón (flancos)
• 📊 Cómo contar y almacenar datos en variables
• 💡 Cómo usar LED como indicador visual

📚 CÓMO FUNCIONAN LOS BOTONES:
─────────────────────────────────────────────────────────────────────────
Un botón simple tiene dos estados:
• ABIERTO (no presionado) = 0V = nivel BAJO
• CERRADO (presionado) = 3.3V = nivel ALTO

Pero hay un problema: los botones tienen "rebotes" (como un resorte
vibrando). Cuando lo presionas, puede dar varios pulsos en milisegundos.

Solución: detectamos "flancos" (cambios de estado), no el estado mismo.
• Flanco de SUBIDA: botón pasa de 0 → 1 (se presiona)
• Flanco de BAJADA: botón pasa de 1 → 0 (se suelta)

📚 PULL-DOWN vs PULL-UP:
─────────────────────────────────────────────────────────────────────────
Los pines GPIO necesitan definirse. Hay dos formas:

• PULL-DOWN: conecta una resistencia interna a GND
   → Cuando el botón NO está presionado, lee 0 (bajo)

• PULL-UP: conecta una resistencia interna a 3.3V
   → Cuando el botón NO está presionado, lee 1 (alto)
   → Y cuando se presiona, lee 0

Nosotros usamos PULL-DOWN porque es más intuitivo: botón = 1.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes:
   • LED (indicador)
   • Resistor 220Ω
   • 2 Botones (pulsadores)

📌 CONEXIONES FÍSICAS:
─────────────────────────────────────────────────────────
   LED indicador:
     GPIO 15 ────► ÁNODO LED
     CÁTODO LED ──► Resistor ──► GND

   Botón + (aumentar contador):
     GPIO 14 ────► Un extremo del botón
     El otro extremo del botón ──► 3.3V (VCC)
     (El pin tiene resistencia PULL-DOWN interna)

   Botón Reset (reiniciar):
     GPIO 13 ────► Un extremo del botón
     El otro extremo del botón ──► 3.3V (VCC)
     (También con PULL-DOWN)

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

# LED indicador: nos muestra si el contador está activo
led = Pin(15, Pin.OUT)
led.value(0)  # Apagado al inicio

# Botón para INCREMENTAR (+1) en GPIO 14
# Pin.PULL_DOWN significa: si no se presiona,默认为 0
boton_mas = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Botón para REINICIAR en GPIO 13
# Misma configuración PULL-DOWN
boton_menos = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Variables del sistema
contador = 0  # El número que contamos
ultimo_estado_mas = 0  # Estado anterior del botón +
ultimo_estado_menos = 0  # Estado anterior del botón -


def mostrar_contador():
    """
    Muestra el valor actual del contador

    Actualiza el LED para indicar si hay actividad
    """
    print(f"📊 Contador: {contador}")

    # LED prendido si el contador es mayor a 0
    led.value(1 if contador > 0 else 0)


# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL - Detectar botones
# ═══════════════════════════════════════════════════════════════════════════

print("🔢 INICIANDO: Contador con Botones")
print("   GPIO 14 → Botón (+) para aumentar")
print("   GPIO 13 → Botón (↻) para reiniciar")
print("=" * 50)

while True:
    # Leer el estado actual de ambos botones
    estado_actual_mas = boton_mas.value()
    estado_actual_menos = boton_menos.value()

    # ─────────────────────────────────────────────────────────────────────
    # DETECCIÓN DE PRESIÓN (flanco de subida)
    # ─────────────────────────────────────────────────────────────────────

    # Botón + (aumentar): si cambió de 0 a 1
    if estado_actual_mas == 1 and ultimo_estado_mas == 0:
        contador += 1

        # Si pasa de 99, volver a 0 (cuenta cíclica)
        if contador > 99:
            contador = 0

        mostrar_contador()
        print("➕ Incrementado (+1)")

    # Botón - (reiniciar): si cambió de 0 a 1
    if estado_actual_menos == 1 and ultimo_estado_menos == 0:
        contador = 0  # Volver a cero
        mostrar_contador()
        print("🔄 Contador REINICIADO")

    # Recordar los estados para la siguiente iteración
    ultimo_estado_mas = estado_actual_mas
    ultimo_estado_menos = estado_actual_menos

    # Pequeña pausa para evitar detección de rebotes
    time.sleep(0.05)
