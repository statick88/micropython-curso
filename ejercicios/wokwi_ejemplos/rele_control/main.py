"""
Relé - El Interruptor que Controla Grandes Cargas
==================================================

¿QUÉS ES UN RELÉ?
Un relé es como un interruptor controlado electrónicamente. Tiene dos
circuitos separados:

• Circuit de CONTROL (chiquito): recibe señales del microcontrolador
• Circuit de POTENCIA (grande): puede manejar voltajes y corrientes altas

Cuando le das señal al relé, INTERNAMENTE conecta dos contactos que
permiten pasar electricidad de alta potencia.

  Microcontrolador → Relé → Electrodomésticos (220V, 10A)

Esto es IMPRESINDIBLE porque:
• El Pico solo puede manejar 3.3V y pocos mA
• No puedes conectar un foco de 220V directamente
• El relé aísla el circuito de control del de potencia (seguridad)

📚 CÓMO FUNCIONA UN RELÉ:
─────────────────────────────────────────────────────────────────────────
Un relé tiene un electroimán внутри:

1. Cuando le das corriente al electroimán (circuito de control)
2. El electroimán atrae un contacto metálico
3.Eso conecta el circuito de alta potencia

  SIN señal → Electroimán desactivado → Contacto abierto → SIN corriente
  CON señal → Electroimán activo → Contacto cerrado → PASA corriente

Los relés tienen especificaciones importantes:
• Voltaje de bobina: 5V (el que usamos)
• Voltaje máximo del contacto: 250V AC (para casas)
• Corriente máxima: 10A (ampers)

⚠️ SEGURIDAD: Los relés de alta voltage pueden ser PELIGROSOS.
Solo úsalos si sabes lo que haces. En este ejemplo simulamos solo.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes:
  • LED indicador + resistor 220Ω
  • Módulo de relé 5V (tipo SRD-05VDC-SL-C)

📌 CONEXIONES FÍSICAS:
─────────────────────────────────────────────────────────
  LED indicador (en la protoboard):
    GPIO 15 ────► ÁNODO LED
    CÁTODO LED ──► Resistor 220Ω ──► GND

  Módulo relé:
    GPIO 14 (Pico) ────► IN (señal de control)
    VBUS (5V Pico) ────► VCC (power del módulo)
    GND (Pico) ─────────► GND

  El relé tiene 3 conexiones de salida (alta potencia):
    • COM (común) - siempre conectado
    • NO (normally open) - abierto cuando no hay señal
    • NC (normally closed) - cerrado cuando no hay señal

  Usamos NO: cuando se activa el relé, conecta COM con NO.

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

# LED: muestra visualmente si el relé está activo
led = Pin(15, Pin.OUT)
led.value(0)  # Apagado al inicio

# Relé en GPIO 14
# ⚠️ IMPORTANTE: Muchos módulos de relé funcionan con LÓGICA INVERTIDA
# Nivel BAJO (0) = activar relé
# Nivel ALTO (1) = desactivar relé
# Esto es porque usan un transistor NPN que requiere eso
rele = Pin(14, Pin.OUT)
rele.value(1)  # Iniciar desactivado (contacto abierto)

# Contador de cambios de estado
cambios = 0


def activar_rele():
    """
    Activa el relé (conecta los contactos)

    En lógica invertida: 0 = activar
    """
    rele.value(0)  # Señal baja para activar
    led.value(1)  # LED indicador prendido
    print("🔋 RELÉ ACTIVADO ✅")
    print("   Contacto: CERRADO (corriente puede pasar)")
    print("   Si estuviera conectado un foco, ¡se prendería!")


def desactivar_rele():
    """
    Desactiva el relé (desconecta los contactos)

    En lógica invertida: 1 = desactivar
    """
    rele.value(1)  # Señal alta para desactivar
    led.value(0)  # LED indicador apagado
    print("⭕ RELÉ DESACTIVADO ❌")
    print("   Contacto: ABIERTO (corriente NO pasa)")
    print("   El dispositivo conectado está apagado")


# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL - Demo de relé
# ═══════════════════════════════════════════════════════════════════════════

print("🔌 INICIANDO: Control de Relé")
print("   GPIO 15 → LED indicador")
print("   GPIO 14 → Módulo relé")
print("=" * 50)
print("ℹ️  Demo: El relé se activa y desactiva cada 2 segundos")
print("   En un proyecto real, conectarías un electrodoméstico")
print("-" * 50)

# Demo: alternar relé cada 2 segundos
while True:
    # Activar (prender)
    activar_rele()
    cambios += 1
    print(f"📍 Ciclo #{cambios}: Relé PRENDIDO por 2 segundos")
    time.sleep(2)

    # Desactivar (apagar)
    desactivar_rele()
    cambios += 1
    print(f"📍 Ciclo #{cambios}: Relé APAGADO por 2 segundos")
    time.sleep(2)

    # Desactivar relé
    desactivar_rele()
    cambios += 1
    print(f"👉 Cambio #{cambios}: Apagado por 2 segundos")
    time.sleep(2)
