"""
Contador con Botones - Raspberry Pi Pico
=========================================
Hardware: Raspberry Pi Pico
Componentes: 2 botones (aumentar/reiniciar), display 7 segmentos
Conexionado: GPIO 15 -> LED, GPIO 14 -> Botón+, GPIO 13 -> BotónReset
Lenguaje: MicroPython
Lógica: Cuenta con un botón, reinicia con otro
"""

from machine import Pin
import time

# Configuración de pines
# LED indicador
led = Pin(15, Pin.OUT)
led.value(0)

# Botón para incrementar (GPIO 14)
boton_mas = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Botón para reiniciar (GPIO 13)
boton_menos = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Contador
contador = 0
ultimo_estado_mas = 0
ultimo_estado_menos = 0


# Función para mostrar número en consola
def mostrar_contador():
    """Muestra el contador actual"""
    print(f"Contador: {contador}")
    # Indicador visual con LED
    led.value(1 if contador > 0 else 0)


# Mensaje inicial
print("=" * 50)
print("Contador con Botones")
print("GPIO 14 = +1, GPIO 13 = Reiniciar")
print("=" * 50)

# Bucle principal
while True:
    # Leer estados de los botones
    estado_mas = boton_mas.value()
    estado_menos = boton_menos.value()

    # Detectar flanco de subida (botón presionar)
    # Flanco de subida: anterior = 0, actual = 1

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
