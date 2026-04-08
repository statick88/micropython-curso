"""
Sensor de Distancia HC-SR04 - Midiendo el Mundo con Ultrasonido
=============================================================

¿QUÉS ES ESTO?
El sensor ultrasónico HC-SR04 es como los murciélos: emite sonidos de alta
frecuencia (ultrasónico) que no podemos escuchar, y mide cuánto tarda en
volver después de rebotar contra un objeto. ¡Con eso calcula la distancia!

📚 CÓMO FUNCIONA EL SENSOR:
─────────────────────────────────────────────────────────────────────────
  1. Enviamos un pulso por el pin TRIGGER (disparador)
  2. El sensor emite 8 pulsos ultrasónicos de 40kHz
  3. El pin ECHO se pone en ALTO mientras el sonido viaja
  4. Cuando el sonido vuelve, ECHO vuelve a BAJO
  5. Medimos el tiempo que estuvo ECHO en alto
  6. Distancia = tiempo × velocidad_del_sonido / 2

  Velocidad del sonido ≈ 343 m/s = 0.0343 cm/μs
  Pero dividimos por 2 porque el sonido fue y volvió

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes: Sensor ultrasónico HC-SR04

📌 CONEXIONES FÍSICAS (¡4 cables nada más!):
─────────────────────────────────────────────────────────
  GPIO 2 (Pico) ──────────► TRIGGER (del sensor) - cable amarillo
  GPIO 3 (Pico) ──────────► ECHO (del sensor)      - cable verde
  VBUS (Pico 5V) ─────────► VCC (del sensor)     - cable rojo
  GND (Pico) ─────────────► GND (del sensor)    - cable negro

  ⚠️ NOTA: El sensor HC-SR04 funciona con 5V, pero el Pico trabaja con 3.3V.
  En Wokwi no hay problema porque simulamos, pero si lo usas en real,
  necesitas un divisor de voltaje para el pin ECHO (5V → 3.3V).

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

from machine import Pin, time_pulse_us
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE PINES
# ─────────────────────────────────────────────────────────────────────────
# TRIGGER: Pin de SALIDA - envía el pulso ultrasónico
trigger = Pin(2, Pin.OUT)

# ECHO: Pin de ENTRADA - recibe el pulso de retorno
# Cuando el sonido vuelve, este pin pasa de 0V a 5V (o 3.3V en nuestro caso)
echo = Pin(3, Pin.IN)


def medir_distancia():
    """
    Mide la distancia al objeto más cercano usando el sensor HC-SR04

    Returns:
        float: Distancia en centímetros (o -1 si no hay detección)
    """
    # 1. Asegurar que el trigger esté en bajo (0V) al inicio
    trigger.value(0)
    time.sleep_us(2)  # Esperar 2 microsegundos para estabilidad

    # 2. Enviar el pulso de triggering de 10 microsegundos
    # Esto activa el sensor para que emita los 8 pulsos ultrasónicos
    trigger.value(1)  # Encender trigger
    time.sleep_us(10)  # Mantener 10μs
    trigger.value(0)  # Apagar trigger

    # 3. Medir el tiempo del pulso de retorno
    # time_pulse_us() mide cuántos microsegundos estuvo el pin en alto
    # El segundo parámetro (1) significa: esperar a que pase a alto
    # El tercer parámetro (30000) es el timeout: máximo 30ms de espera
    try:
        duracion = time_pulse_us(echo, 1, 30000)

        # 4. Calcular la distancia
        # fórmula: tiempo × velocidad / 2
        # duracion está en microsegundos
        # 343 m/s = 0.0343 cm/μs → pero vamos y vengamos → /2
        # Simplificado: duracion × 0.01715
        distancia = duracion * 0.01715

        return distancia
    except OSError:
        # Timeout: el sonido no volvió dentro de 30ms
        # Esto significa que no hay objeto en el rango de medición (hasta 4m)
        return -1


def obtener_distancia_formateada():
    """
    Obtiene la distancia y la presenta de forma legible

    Returns:
        str: Distancia formateada o mensaje de error
    """
    distancia = medir_distancia()

    if distancia < 0:
        return "⚠️ Sin detección (objeto muy lejos)"
    elif distancia > 400:
        return "📍 Fuera de rango (>4 metros)"
    else:
        return f"📏 {distancia:.2f} cm"


# ═══════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("🌊 INICIANDO: Sensor de Distancia HC-SR04")
print("   Midiendo distancia cada 500ms")
print("   El sensor emite ultrasonido y mide el eco")
print("-" * 50)

while True:
    distancia = medir_distancia()

    if distancia < 0:
        print("⚠️  Sin detección de objeto")
    elif distancia > 400:
        print("📍 Objeto fuera de rango (>400cm)")
    else:
        # Crear una representación visual con barras
        # Cada 10cm = un bloque █
        barras = "█" * int(distancia / 10)
        print(f"📏 Distancia: {distancia:6.2f} cm | {barras}")

    time.sleep(0.5)  # Esperar 500ms entre mediciones
