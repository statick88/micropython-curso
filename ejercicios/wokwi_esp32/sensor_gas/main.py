"""
💨 Sensor de Gas MQ-2 - ESP32 con MicroPython
=============================================

¿QUÉ HACE ESTE PROYECTO?
Este ejemplo enseña cómo detectar presencia de gases inflamables y tóxicos usando un sensor MQ-2,
activando una alarma visual (LED) cuando los niveles superan umbrales de seguridad.
Es como darle al ESP32 un "sentido del olfato" para detectar peligros invisibles.

🧠 CÓMO FUNCIONA TÉCNICAMENTE:
1. El sensor MQ-2 contiene un elemento sensible que cambia su resistencia según la concentración de gases
2. En aire limpio: resistencia ALTA → poco flujo de corriente
3. En presencia de gases: resistencia BAJA → más flujo de corriente
4. Lo conectamos en configuración divisor de tensión para medir el cambio de voltaje
5. Usamos el ADC del ESP32 para convertir ese voltaje a un valor digital (0-4095)
6. Aplicamos umbrales para clasificar el nivel de peligro y activar una alarma LED
7. Promediamos múltiples lecturas para reducir ruido y obtener lecturas más estables

🔧 CONEXIONES FÍSICAS:
CIRCUITO DIVIDOR DE TENSIÓN MQ-2:
[3.3V] ──[MQ-2 ]───────●────[220Ω]──[GND]
                      │
                  [GPIO34] ← Lecture del voltaje (ADC)

LED DE ALARMA CON RESISTENCIA PROTECTORA:
[GPIO2] ──[220Ω]──|>|──[GND]
                  LED

Donde:
- MQ-2: Sensor de gas que cambia resistencia según concentración
- 220Ω: Resistencia fija para formar divisor de tensión
- LED: Indicador visual de alarma (rojo = peligro)
- GPIO34: Entrada analógica (ADC) para leer nivel de gas
- GPIO2: Salida digital para controlar el LED de alarma

⚠️  GASES DETECTABLES POR MQ-2:
- Hidrógeno (H₂) - Muy inflamable
- LPG (Propano/Butano) - Gas de cocina y calefacción
- Metano (CH₄) - Gas natural
- Humo de fuego - Partículas de combustión
- Alcohol - Vapores etílicos
- Monóxido de carbono (CO) - Gas tóxico incoloro

📱 QUÉ VERÁS EN CONSOLA:
- Valor promedio del sensor MQ-2 (0-4095, más alto = más gas)
- Clasificación de nivel: ✅ SEGURO, ⚠️ ADVERTENCIA, 🚨 PELIGRO!, 💀 PELIGRO CRÍTICO!
- Estado de la alarma LED: 🚨 ALARMA o ⚫ OK
- Representación visual de barras que crecen con más gas
- Actualización cada 500ms para balance entre respuesta y estabilidad

⚠️  NOTAS IMPORTANTES DE SEGURIDAD Y CALIBRACIÓN:
- Este es un proyecto educativo - NO usar para detección real de gas en hogares
- Los umbrales son aproximados y requieren calibración según entorno específico
- El sensor necesita tiempo de calentamiento (~1-2 min) para lecturas estables
- Evitar exposición prolongada a altas concentraciones que puedan dañar el sensor
- Siempre verificar con equipos certificados para aplicaciones de seguridad reales
"""

from machine import Pin, ADC
import time

# ============================================
# CONFIGURACIÓN DE PINES GPIO
# ============================================

# LED INDICADOR DE ALARMA
# Conectamos el LED mediante una resistencia limitadora (220Ω típica)
# para protegerlo de corriente excesiva
led = Pin(2, Pin.OUT)
led.value(0)  # Iniciamos con LED apagado (estado seguro)

# SENSOR MQ-2 CONFIGURADO COMO ENTRADA ANALÓGICA
# Los pines 34-39 del ESP32 son solo de entrada (no salida), perfecto para sensores analógicos
sensor_gas = ADC(Pin(34))

# Configuramos atenuación para usar rango completo 0-3.3V
# Esto nos da la máxima sensibilidad para detectar cambios sutiles
sensor_gas.atten(ADC.ATTN_11DB)  # Rango: 0-3.3V (ideal para nuestro divisor de tensión)

# ============================================
# CONSTANTES DE UMBRALES DE DETECCIÓN
# ============================================

# Estos valores son PUNTOS DE PARTIDA - requieren calibración ambiental
# En aire limpio típico: lecturas entre 100-300 (varía según humedad, temperatura, etc.)
# Los valores deben ajustarse mediante experimentación en tu entorno específico

UMBRAL_SEGURO = 500  # Lecturas por debajo: ambiente considerado seguro
UMBRAL_PELIGRO = 1500  # Lecturas entre 500-1500: nivel de alerta preventiva
UMBRAL_DANGER = 3000  # Lecturas entre 1500-3000: concentración peligrosa detectada
# Lecturas > 3000: concentración muy alta - riesgo inmediato


def leer_gas():
    """
    📏 Lee y promedia múltiples lecturas del sensor MQ-2 para estabilidad

    📖 Por qué promediar:
    - Los sensores de gas tienen ruido inherente en sus lecturas
    - Factores como temperatura y humedad afectan la resistencia base
    - Promediar reduce variaciones aleatorias y da lecturas más confiables
    - 10 muestras con 10ms entre ellas = 100ms total de muestreo

    🔬 Proceso de medición:
    1. Tomamos 10 lecturas rápidas sucesivas del ADC
    2. Esperamos 10ms entre lecturas para permitir estabilización
    3. Sumamos todas las lecturas y calculamos el promedio entero
    4. Devolvemos el valor promedio como representación estable

    Returns:
        int: Valor promedio entre 0-4095 representando concentración de gas
    """
    total = 0
    for i in range(10):  # Tomar 10 muestras
        total += sensor_gas.read()  # Lectura cruda del ADC (0-4095)
        time.sleep(0.01)  # Pausa breve entre lecturas
    return total // 10  # División entera para promedio


def obtener_nivel_gas(valor):
    """
    🎯 Clasifica el valor crudo del sensor en niveles de riesgo descriptivos

    📋 Escalas típicas MQ-2 en aire ambiente:
    - 0-500:      Aire limpio, lectura de ruido/fondo
    - 500-1500:   Presencia detectable de gases (posibles fugas menores)
    - 1500-3000:  Concentración significativa - requiere investigación
    - 3000+:      Concentración alta - posible peligro inmediato

    📝 IMPORTANTE: Estos rangos son aproximados y dependen de:
    - Tipo específico de gas presente (cada gas tiene diferente respuesta)
    - Temperatura y humedad ambiente
    - Tiempo de calentamiento y edad del sensor
    - Calibración individual del sensor

    Args:
        valor (int): Valor promedio leído del ADC (0-4095)

    Returns:
        str: Descripción legible con emoji del nivel de riesgo
    """
    if valor < UMBRAL_SEGURO:
        return "✅ SEGURO"  # Lecturas normales de fondo
    elif valor < UMBRAL_PELIGRO:
        return "⚠️ ADVERTENCIA"  # Detección temprana de posibles fugas
    elif valor < UMBRAL_DANGER:
        return "🚨 PELIGRO!"  # Concentración que requiere atención inmediata
    else:
        return "💀 PELIGRO CRÍTICO!"  # Nivel potencialmente peligroso


# ============================================
# MENSAJE DE INICIALIZACIÓN
# ============================================
print("=" * 70)
print("💨 EJEMPLO: Detección de Gases con Sensor MQ-2")
print("👃‍🗨️  Dale al ESP32 un sentido del 'olfato' para peligros invisibles")
print("=" * 70)
print("📋 Conexiones verificadas:")
print("   🔴 GPIO 2  → LED de alarma (con resistencia 220Ω protección)")
print("   🟡 GPIO 34 → MQ-2 Sensor de Gas (en divisor de tensión)")
print("   🔴 MQ-2 VCC → 3.3V")
print("   ⚫ MQ-2 GND  → GND")
print("   ⚫ LED GND   → GND (a través de resistencia protectora)")
print("=" * 70)
print("⚠️  ADVERTENCIA IMPORTANTE:")
print("   Este es un proyecto EDUCATIVO de demostración")
print("   NO usar para detección real de gas en aplicaciones de seguridad")
print("   Los umbrales requieren calibración específica por entorno")
print("   Siempre usar equipos certificados para detección real de riesgos")
print("=" * 70)
print("🧪 Experimentos sugeridos (con PRECAUCIÓN):")
print("   1. Soplar suavemente cerca del sensor (aliento contiene CO₂ y humedad)")
print("   2. Acercar un marcador abierto (alcohol volátil) a distancia segura")
print("   3. Observar cómo cambian las lecturas con diferentes sustancias")
print("   4. NOTA: Nunca exponer el sensor a concentraciones altas o peligrosas")
print("=" * 70)
print("📈 Lecturas esperadas en condiciones normales:")
print("   - Aire limpio interior: 100-400")
print("   - Cerca de cocina con gas: 500-1200 (varía mucho)")
print("   - Humo de cigarrillo cercano: 800-2000+")
print("   - Estos son solo ejemplos - CALIBRE SU ENTORNO ESPECÍFICO")
print("=" * 70)


# ============================================
# BUCLE PRINCIPAL DE DETECCIÓN Y ALARMA
# ============================================
while True:
    # LEER Y PROMEDIAR EL SENSOR DE GAS
    valor_gas = leer_gas()
    nivel_riesgo = obtener_nivel_gas(valor_gas)

    # ACTIVAR ALARMA VISUAL SEGÚN NIVEL DE RIESGO
    # Encendemos el LED cuando detectamos niveles potencialmente peligrosos
    if valor_gas >= UMBRAL_PELIGRO:
        # UMBRAL_PELIGRO o superior: activar alarma
        led.value(1)
        estado_alarma = "🚨 ALARMA ACTIVADA"
    else:
        # Por debajo del umbral: mantenerLED apagado (estado normal)
        led.value(0)
        estado_alarma = "⚫ MONITOREO NORMAL"

    # MOSTRAR INFORME COMPLETO EN CONSOLA
    print(f"📊 Valor MQ-2: {valor_gas:4d} | 🎯 Nivel: {nivel_riesgo} | {estado_alarma}")

    # CREAR REPRESENTACIÓN VISUAL DEL NIVEL DE GAS
    # Usamos dos estilos según el rango para mejor visualización
    if valor_gas < 1000:
        # Para valores bajos: mostrar progresión con bloques claros y oscuros
        bloques_oscuros = "░" * int((valor_gas / 1000) * 10)  # Hasta 10 bloques oscuros
        bloques_claros = "█" * 3  # Siempre mostrar 3 de referencia
        barra_visual = bloques_oscuros + bloques_claros
    else:
        # Para valores altos: usar bloques sólidos, limitando a longitud fija
        longitud_barras = min(int((valor_gas / 4095) * 30), 30)  # Máximo 30 bloques
        barra_visual = "█" * longitud_barras

    print(f"  📈 Nivel: {barra_visual:<35}")
    print("-" * 60)

    # Esperar antes de la siguiente lectura
    # 500ms = 2 lecturas por segundo (buen balance entre respuesta y estabilidad)
    # Tiempo suficiente para que el sensor se estabilice entre lecturas
    time.sleep(0.5)
