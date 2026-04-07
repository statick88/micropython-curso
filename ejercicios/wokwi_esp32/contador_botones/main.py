"""
Contador con Botones - ESP32
============================
Hardware: ESP32 DevKit V1
Componentes: 2 botones (aumentar/reiniciar), LED indicador
Conexionado: GPIO 2 -> LED, GPIO 4 -> Botón+, GPIO 5 -> BotónReset
Lenguaje: MicroPython
Lógica: Cuenta con un botón, reinicia con otro
"""

from machine import Pin
import time

# Configuración de pines
# LED indicador (GPIO 2 - LED integrado)
led = Pin(2, Pin.OUT)
led.value(0)

# Botón para incrementar (GPIO 4)
boton_mas = Pin(4, Pin.IN, Pin.PULL_DOWN)

# Botón para reiniciar (GPIO 5)
boton_menos = Pin(5, Pin.IN, Pin.PULL_DOWN)

# Contador
contador = 0
ultimo_estado_mas = 0
ultimo_estado_menos = 0


def mostrar_contador():
    """Muestra el contador actual"""
    print(f"Contador: {contador}")
    led.value(1 if contador > 0 else 0)


# Mensaje inicial
print("=" * 50)
print("Contador con Botones - ESP32")
print("GPIO 4 = +1, GPIO 5 = Reiniciar")
print("=" * 50)

# Bucle principal
while True:
    # Leer estados de los botones
    estado_mas = boton_mas.value()
    estado_menos = boton_menos.value()

    # Botón + (aumentar)
    if estado_mas == 1 and ultimo_estado_mas == 0:
        contador += 1
        if contador > 99:
            contador = 0
        mostrar_contador()
        print("➕ +1")

    # Botón - (reiniciar)
    if estado_menos == 1 and ultimo_estado_menos == 0:
        contador = 0
        mostrar_contador()
        print("🔄 REINICIADO")

    # Actualizar estados anteriores
    ultimo_estado_mas = estado_mas
    ultimo_estado_menos = estado_menos

    # Pequeña pausa para evitar rebotes
    time.sleep(0.05)
