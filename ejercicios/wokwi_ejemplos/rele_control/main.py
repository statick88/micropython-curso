"""
Control de Relé - Raspberry Pi Pico
===================================
Hardware: Raspberry Pi Pico
Componentes: 1 LED, 1 resistor, 1 módulo relé 5V
Conexionado: GPIO 15 -> LED, GPIO 14 -> Relé
Lenguaje: MicroPython
Lógica: Controla un relé para activar/disactivar dispositivos
"""

from machine import Pin
import time

# Configuración de pines
# LED indicador
led = Pin(15, Pin.OUT)
led.value(0)

# Relé en GPIO 14
# El relé se activa con nivel bajo (invertido)
rele = Pin(14, Pin.OUT)
rele.value(1)  # Iniciar desactivado (relé abierto)

# Contador de cambios
cambios = 0


def activar_rele():
    """Activa el relé (enciende el LED del relé)"""
    rele.value(0)  # Nivel bajo activa el relé
    led.value(1)  # LED indicador
    print("🔋 RELÉ ACTIVADO - Contacto cerrado")


def desactivar_rele():
    """Desactiva el relé (apaga el LED del relé)"""
    rele.value(1)  # Nivel alto desactiva el relé
    led.value(0)  # LED indicador
    print("⭕ RELÉ DESACTIVADO - Contacto abierto")


# Mensaje inicial
print("=" * 50)
print("Control de Relé")
print("GPIO 15 -> LED indicador, GPIO 14 -> Relé")
print("=" * 50)

# Bucle principal
while True:
    # Activar relé
    activar_rele()
    cambios += 1
    print(f"👉 Cambio #{cambios}: Encendido por 2 segundos")
    time.sleep(2)

    # Desactivar relé
    desactivar_rele()
    cambios += 1
    print(f"👉 Cambio #{cambios}: Apagado por 2 segundos")
    time.sleep(2)
