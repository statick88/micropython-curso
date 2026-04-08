"""
💡 Sensor de Luz LDR - ESP32 con MicroPython
============================================

¿QUÉ HACE ESTE PROYECTO?
Este ejemplo muestra cómo medir la intensidad de luz ambiental usando un LDR
(Light Dependent Resistor o fotorresistor) y controlar un LED basado en esa lectura.
Es como darle al ESP32 un "sentido de la vista" muy básico.

🧠 CÓMO FUNCIONA TÉCNICAMENTE:
1. El LDR cambia su resistencia según la cantidad de luz que recibe:
   - En oscuridad: resistencia ALTA (poco flujo de electrones)
   - En luz: resistencia BAJA (mucho flujo de electrones)
2. Lo conectamos como divisor de tensión con una resistencia fija
3. Medimos la tensión en el punto medio con un ADC (Conversor Analógico-Digital)
4. Ese valor nos indica cuánta luz hay ambiente
5. Encendemos el LED cuando está oscuro y lo apagamos cuando hay luz
   (funciona como una lámpara de noche automática)

🔧 CONEXIONES FÍSICAS:
CIRCUITO DIVIDOR DE TENSIÓN LDR:
[3.3V] ──[LDR ]───────●────[220Ω]──[GND]
                      │
                  [GPIO34] ← Lectura del voltaje

LED CON RESISTENCIA DE PROTECCIÓN:
[GPIO2] ──[220Ω]──|>|──[GND]
                  LED

Donde:
- LDR: Fotorresistor (cambia resistencia con luz)
- 220Ω: Resistencia fija para formar divisor de tensión
- LED: Diodo emisor de luz con su resistencia limitadora de corriente
- GPIO2: Salida digital para controlar el LED
- GPIO34: Entrada analógica (ADC) para leer el nivel de luz

📱 QUÉ VERÁS EN CONSOLA:
- Valor numérico del LDR (0-4095 para 12-bit ADC)
- Clasificación del nivel de luz: 🌑 OSCURO, 🌤️ PENUMBRA, ☀️ NORMAL, 💡 MUY BRILLANTE
- Estado del LED: 💡 ENCENDIDO o ⚫ APAGADO
- Representación visual de barras que crecen con más luz
- Actualización cada 200ms para respuesta rápida

⚠️  NOTAS IMPORTANTES:
- El GPIO34 es solo de entrada (no se puede usar como salida)
- Usamos atenuación ATTN_11DB para rango completo 0-3.3V
- El umbral de 1500 es empírico - ajústalo según tu LDR y condiciones de luz
"""

from machine import Pin, ADC
import time

# ============================================
# CONFIGURACIÓN DE PINES GPIO
# ============================================

# LED: Salida digital para controlarlo
# Conectamos el LED mediante una resistencia limitadora (220Ω típica)
# para evitar que reciba demasiada corriente y se queme
led = Pin(2, Pin.OUT)
led.value(0)  # Iniciamos con el LED apagado

# LDR: Entrada analógica conectada en configuración divisor de tensión
# El GPIO34 solo puede ser entrada, perfecto para leer sensores analógicos
ldr = ADC(Pin(34))

# Configuramos la atenuación del ADC para usar todo el rango 0-3.3V
# Otras opciones: ATTN_0DB (0-1.2V), ATTN_2_5DB (0-1.5V), ATTN_6DB (0-2.2V)
ldr.atten(ADC.ATTN_11DB)  # Rango completo: 0-3.3V (ideal para nuestro divisor)

# ============================================
# CONSTANTES DE CONFIGURACIÓN
# ============================================

# Umbral para decidir cuándo está "oscuro enough" para encender el LED
# Este valor depende de:
# - Características específicas de tu LDR
# - Resistencia fija usada en el divisor (220Ω en nuestro caso)
# - Condiciones de iluminación ambiente
# ¡Ajusta este valor mediante experimentación!
UMBRAL_OSCURO = 1500  # Valores típicos: 1000-2500 según circuito y ambiente


def leer_luz():
    """
    🔆 Lee el valor crudo del sensor LDR a través del ADC

    📖 Explicación:
    - El ADC convierte el voltaje analógico (0-3.3V) a un número digital
    - Con atenuación 11DB y resolución de 12 bits: 0-4095
    - 0 = 0V (máxima luz, LDR resistencia mínima)
    - 4095 = 3.3V (oscuridad total, LDR resistencia máxima)

    Returns:
        int: Valor entre 0 y 4095 representando el nivel de luz
    """
    return ldr.read()


def obtener_nivel_luz(valor):
    """
    📊 Clasifica el valor crudo del LDR en niveles descriptivos de luz

    📋 Escalas típicas (pueden variar según tu LDR específico):
    - 0-1000:     Luz muy brillante (luz solar directa, foco cercano)
    - 1000-2000:  Luz normal (iluminación interior típica, día nublado)
    - 2000-3500:  Penumbra (iluminación tenue, lejos de ventanas)
    - 3500-4095:  Oscuridad (habitación sin luces, noche)

    Args:
        valor (int): Valor crudo leído del ADC (0-4095)

    Returns:
        str: Descripción legible con emoji del nivel de luz
    """
    if valor < 1000:
        return "🌑 OSCURO"  # Muy poca luz reflejada (mucho voltaje)
    elif valor < 2000:
        return "🌤️ PENUMBRA"  # Luz ambiental tenue
    elif valor < 3500:
        return "☀️ NORMAL"  # Iluminación estándar de interior
    else:
        return "💡 MUY BRILLANTE"  # Mucha luz incidente (poca resistencia LDR)


# ============================================
# MENSAJE DE INICIALIZACIÓN
# ============================================
print("=" * 60)
print("💡 EJEMPLO: Sensor de Luz LDR con Control de LED")
print("👁️‍🗨️  Dale al ESP32 un sentido básico de 'visión'")
print("=" * 60)
print("📋 Conexiones verificadas:")
print("   🔴 GPIO 2  → LED (con resistencia 220Ω en serie)")
print("   🟡 GPIO 34 → LDR (en divisor de tensión con 220Ω)")
print("   🔴 LDR VCC → 3.3V")
print("   ⚫ LDR GND  → GND")
print("   ⚫ LED GND  → GND (a través de su resistencia)")
print("=" * 60)
print("💡 Cómo funciona:")
print("   - En oscuridad: LDR resistencia ALTA → más voltaje en GPIO34")
print("   - En luz:     LDR resistencia BAJA → menos voltaje en GPIO34")
print("   - LED se enciende cuando lectura < UMBRAL_OSCURO (oscuridad)")
print("=" * 60)
print("🧪 Experimentos sugeridos:")
print("   1. Cubrir el LDR con el dedo → debería encender el LED")
print("   2. Apuntar una linterna al LDR → debería apagar el LED")
print("   3. Cambiar el umbral y observar cómo afecta al comportamiento")
print("   4. Medir valores en diferentes condiciones de luz")
print("=" * 60)


# ============================================
# BUCLE PRINCIPAL DE LECTURA Y CONTROL
# ============================================
while True:
    # LEER EL SENSOR DE LUZ
    valor_ldr = leer_luz()
    nivel_luz = obtener_nivel_luz(valor_ldr)

    # DECIDIR ESTADO DEL LED SEGÚN NIVEL DE LUZ
    if valor_ldr < UMBRAL_OSCURO:
        # Condición OSCURO: encender LED
        led.value(1)
        estado_led = "💡 ENCENDIDO"
    else:
        # Condición CLARO: apagar LED (ahorramos energía)
        led.value(0)
        estado_led = "⚫ APAGADO"

    # MOSTRAR INFORMACIÓN COMPLETA EN CONSOLA
    print(f"🔢 Valor LDR: {valor_ldr:4d} | 💡 Nivel: {nivel_luz} | {estado_led}")

    # CREAR BARRA VISUAL PARA INTUICIÓN RÁPIDA
    # Escalamos para que el máximo valor (4095) dé ~40 bloques
    longitud_barra = int((valor_ldr / 4095) * 40)
    barra_visual = "█" * longitud_barra
    # Mostrar también el porcentaje para referencia
    porcentaje = (valor_ldr / 4095) * 100
    print(f"  📊 Luz: {barra_visual:<40} ({porcentaje:5.1f}%)")
    print("-" * 50)

    # Esperar antes de la siguiente lectura
    # 200ms = 5 lecturas por segundo (suficiente para detectar cambios rápidos)
    time.sleep(0.2)
