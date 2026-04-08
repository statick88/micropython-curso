"""
🔍 Sensor de Distancia HC-SR04 - ESP32 con MicroPython
==================================================

¿QUÉ HACE ESTE PROYECTO?
Este ejemplo enseña cómo medir distancias usando un sensor ultrasónico HC-SR04,
el mismo tipo de tecnología que usan los murciélagos para navegar en la oscuridad
(y que también se encuentra en algunos autos para ayudar a estacionar).

🧠 CÓMO FUNCIONA TÉCNICAMENTE:
1. El sensor emite un pulso de sonido ultrasónico (inaudible para humanos)
2. Ese sonido viaja por el aire, choca con un objeto y regresa como eco
3. Medimos cuánto tardó el sonido en ir y venir
4. Conociendo la velocidad del sonido, calculamos la distancia:
   distancia = (tiempo × velocidad) / 2
   (dividimos por 2 porque el sonido hizo el viaje ida y vuelta)

🔧 CONEXIONES FÍSICAS:
- ESP32 GPIO 5  → TRIG (Trigger) del HC-SR04 [CABLE AMARILLO]
  Envía la orden de "¡emite el pulso ultrasónico ahora!"
- ESP32 GPIO 18 → ECHO (Echo) del HC-SR04 [CABLE VERDE]
  Recibe la señal de "¡aquí llegó el eco!"
- HC-SR04 VCC   → ESP32 3.3V [CABLE ROJO]
  Alimentación del sensor
- HC-SR04 GND   → ESP32 GND [CABLE NEGRO]
  Referencia de tierra/ground

📱 QUÉ VERÁS EN CONSOLA:
- Medición de distancia cada 0.5 segundos
- Representación visual con bloques (█) para intuir la distancia
- Alertas cuando no hay detección o el objeto está muy lejos
- Valores numéricos precisos en centímetros

⚠️  LIMITACIONES DEL SENSOR:
- Rango efectivo: 2cm a 400cm
- Menos preciso con objetos muy pequeños, blandos o en ángulo
- Puede fallar en ambientes muy ruidosos acústicamente
"""

from machine import Pin, time_pulse_us
import time

# ============================================
# CONFIGURACIÓN DE PINES GPIO
# ============================================

# TRIGGER: Pin que ENVÍA el pulso ultrasónico
# Cuando ponemos este pin en HIGH durante 10µs, le decimos al sensor:
# "¡Genera ahora un pulso de sonido ultrasónico!"
trigger = Pin(5, Pin.OUT)

# ECHO: Pin que RECIBE el pulso de retorno
# El sensor pone este pin en HIGH mientras espera el eco
# Lo medimos para saber cuánto tardó el sonido en regresar
echo = Pin(18, Pin.IN)

# Iniciamos con trigger en LOW (estado de reposo)
trigger.value(0)


def medir_distancia():
    """
    🎯 Mide la distancia al objeto más cercano usando el sensor HC-SR04

    📖 Explicación paso a paso:
    1. Ponemos TRIG en LOW para asegurar estado limpio
    2. Enviamos pulso de 10µs en TRIG (activa el sensor)
    3. El sensor emite 8 ciclos de ultrasonido a 40kHz
    4. Esperamos que el sonido viaje, choque y regrese como eco
    5. Medimos cuánto tiempo estuvo el pin ECHO en HIGH
    6. Convertimos ese tiempo a distancia usando la velocidad del sonido

    📐 FÓRMULA:
    Distancia = (Tiempo × Velocidad_del_sonido) / 2
    Donde:
    - Tiempo: microsegundos que duró el pulso ECHO
    - Velocidad_del_sonido: 0.0343 cm/µs (343 m/s)
    - Dividimos por 2 porque el sonido va y viene

    Returns:
        float: Distancia en centímetros, -1 si hay error (timeout)
    """
    # PASO 1: Asegurar estado inicial limpio
    trigger.value(0)
    time.sleep_us(2)  # Espera breve para estabilización

    # PASO 2: Enviar pulso de triggering (10 microsegundos HIGH)
    # Este es el "¡dispara ahora!" al sensor
    trigger.value(1)
    time.sleep_us(10)  # Pulso preciso de 10µs
    trigger.value(0)  # Volver a LOW

    # PASO 3: Medir el pulso de retorno en ECHO
    try:
        # time_pulse_us(pin, nivel, timeout)
        # Espera hasta que el pin llegue al nivel especificado (1=HIGH)
        # y mide cuánto tiempo permanece en ese nivel
        # Timeout de 30000µs = 30máx correspondiente a ~5m de distancia
        duracion = time_pulse_us(echo, 1, 30000)

        # PASO 4: Convertir tiempo a distancia
        # Fórmula: distancia = tiempo × velocidad_sonido / 2
        distancia = duracion * 0.0343 / 2

        return distancia

    except OSError:
        # Esto ocurre si time_pulse_us agota el timeout
        # Significa que no recibió eco dentro del tiempo esperado
        # (objeto demasiado lejos o ninguna reflexión detectada)
        return -1


# ============================================
# MENSAJE DE INICIALIZACIÓN
# ============================================
print("=" * 60)
print("🔍 EJEMPLO: Sensor de Distancia HC-SR04")
print("📡 Tecnología de ultrasonido - Como el sonar de los murciélagos")
print("=" * 60)
print("📋 Conexiones verificadas:")
print("   🟡 GPIO 5  → TRIG (Trigger)")
print("   🟢 GPIO 18 → ECHO (Echo)")
print("   🔴 VCC     → 3.3V")
print("   ⚫ GND    → GND")
print("=" * 60)
print("💡 Tips:")
print("   - Acercar/alejar objetos frente al sensor")
print("   - El sensor funciona mejor con superficies duras y planas")
print("   - Rango práctico: 2cm - 400cm")
print("=" * 60)


# ============================================
# BUCLE PRINCIPAL DE MEDICIÓN
# ============================================
while True:
    distancia = medir_distancia()

    if distancia < 0:
        # CASO 1: Timeout - No se detectó eco
        print("⚠️  Sin detección - Verifique conexiones o acerque un objeto")

    elif distancia > 400:
        # CASO 2: Fuera de rango máximo especifico del sensor
        print("📍 Objeto detectado pero fuera de rango (>400cm)")
        print("   (El HC-SR04 tiene límite teórico de ~400cm)")

    else:
        # CASO 3: Medición válida - Mostrar resultado

        # Crear barra visual proporcional para intuición rápida
        # Escalamos para que 40cm = ~4 bloques (ajustable según preferencia)
        longitud_barra = min(int(distancia / 10), 40)  # Máximo 40 bloques
        barra_visual = "█" * longitud_barra

        # Icono según proximidad
        if distancia < 10:
            icono = "🚨"  # Muy cerca
        elif distancia < 30:
            icono = "⚠️"  # Cercano
        elif distancia < 100:
            icono = "📏"  # Distancia media
        else:
            icono = "🔍"  # Lejos

        print(f"{icono} Distancia: {distancia:6.2f} cm |{barra_visual:<40}|")

    # Esperar antes de la siguiente medición
    # 500ms = 2 lecturas por segundo (suave para observación)
    time.sleep(0.5)
