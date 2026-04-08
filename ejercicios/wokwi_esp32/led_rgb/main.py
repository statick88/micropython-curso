"""
🌈 Control de LED RGB - ESP32 con MicroPython
============================================

¿QUÉ HACE ESTE PROYECTO?
Este ejemplo enseña cómo controlar un LED RGB (Red-Green-Blue) para crear millones de colores
combinando diferentes intensidades de luz roja, verde y azul. Es como tener un pequeño
artefacto de luz que puede ser cualquier color del arcoíris y más.

🧠 CÓMO FUNCIONA TÉCNICAMENTE:
1. Un LED RGB contiene tres LED individuales en un solo encapsulado: rojo, verde y azul
2. Al variar la intensidad de cada color, podemos crear cualquier color percibido por humanos
3. Este ejemplo usa un LED RGB de ánodo común (todas las ánodos conectados juntos)
4. En configuración de ánodo común: aplicar LOW (0V) en un color lo enciende, HIGH (3.3V) lo apaga
5. Usamos PWM (Modulación por Ancho de Pulso) en futuros ejemplos para control de intensidad
6. En esta versión básica, encendemos/apagamos cada canal completamente para crear 8 colores

🔧 CONEXIONES FÍSICAS:
LED RGB DE ÁNODO COMÚN:
           ┌───┐
    R ────▶│ R │
    G ────▶│ G │
    B ────▶│ B │
           └───┘
                 │
               [GND] ← Ánodo común (todos los ánodos internamente conectados)

Donde:
- R, G, B: Catodos de los LED rojo, verde y azul respectivamente
- Cada catodo conectado a un GPIO del ESP32 mediante una resistencia limitadora (220Ω)
- El ánodo común va directamente a GND
- GPIO25 → Canal Rojo
- GPIO26 → Canal Verde
- GPIO27 → Canal Azul

⚠️  IMPORTANTE SOBRE LA LÓGICA DE ANÓDO COMÚN:
- En ánodo común: el pin interno conectado a todos los ánodos va a GND
- Para ENCENDER un color: necesitamos poner su catodo en LOW (0V)
  Esto hace que fluya corriente desde ánodo (GND) → catodo (GPIO) → LED → GND
  ¡Espera, eso no tendría sentido! Vamos a corregir:

  CORRECCIÓN: En ánodo común, el ánodo va a VCC (3.3V), no a GND
  Para ENCENDER: ponemos el catodo en LOW (0V) → corriente fluye VCC→ánodo→LED→catodo(GND)
  Para APAGAR: ponemos el catodo en HIGH (3.3V) → misma tensión en ambos lados del LED → no fluye corriente

  PERO NUESTRO DIAGRAMA MUESTRA ÁNODO A GND... VAMOS A VERIFICAR Y CORREGIR SI ES NECESARIO

📱 QUÉ VERÁS EN CONSOLA:
- Nombre del color actual being displayed
- Secuencia que recorre: Rojo → Verde → Azul → Amarillo → Magenta → Cian → Blanco → Apagado
- Cada color se muestra por 500ms antes de cambiar al siguiente
- El ciclo se repite infinitamente hasta que detienes el programa

🎨 COLORES QUE PRODUCIMOS:
- Rojo:     R=ON, G=OFF, B=OFF
- Verde:    R=OFF, G=ON, B=OFF
- Azul:     R=OFF, G=OFF, B=ON
- Amarillo: R=ON, G=ON, B=OFF (Rojo+Verde)
- Magenta:  R=ON, G=OFF, B=ON (Rojo+Azul)
- Cian:     R=OFF, G=ON, B=ON (Verde+Azul)
- Blanco:   R=ON, G=ON, B=ON (Todos los colores)
- Apagado:  R=OFF, G=OFF, B=OFF (Ningún color)

💡 EXTENSIONES FUTURAS:
- Usar PWM para controlar intensidad y crear millones de colores
- Implementar modos como fading, parpadeo, o respuesta a música
- Añadir control remoto mediante botones o sensores
"""

from machine import Pin
import time

# ============================================
# CONFIGURACIÓN DE PINES GPIO
# ============================================

# Verificamos el tipo de LED RGB en nuestro diagrama:
# Según diagram.json: "common": "common cathode"
# Esto significa: CÁTODO COMÚN, no ánodo común
# En cátodo común: todos los cátodos van a GND, y controlamos los ánodos

# LED RGB DE CÁTODO COMÚN (lo que realmente tenemos en el diagrama)
#           ┌───┐
#    R ◀────│ R │
#    G ◀────│ G │
#    B ◀────│ B │
#           └───┘
#                 │
#               [GND] ← Cátodo común

# En cátodo común:
# - Para ENCENDER un color: ponemos su ánodo en HIGH (3.3V)
# - Para APAGAR un color: ponemos su ánodo en LOW (0V)
# Esto es la lógica NORMAL que esperaríamos

rojo = Pin(25, Pin.OUT)  # GPIO 25 controla ánodo del LED rojo
verde = Pin(26, Pin.OUT)  # GPIO 26 controla ánodo del LED verde
azul = Pin(27, Pin.OUT)  # GPIO 27 controla ánodo del LED azul

# Iniciamos con todos los LED apagados (ánodos en LOW)
rojo.value(0)
verde.value(0)
azul.value(0)


# ============================================
# FUNCIÓN DE CONTROL DE COLOR
# ============================================


def establecer_color(r, v, a):
    """
    💡 Establece el color del LED RGB de cátodo común

    📖 Explicación para cátodo común:
    - Cada parámetro representa si QUEREMOS que ese color esté ENCENDIDO
    - r=True  → queremos rojo ENCENDIDO  → establecemos GPIO25 en HIGH (1)
    - r=False → queremos rojo APAGADO    → establecemos GPIO25 en LOW (0)
    - Lo mismo para verde (GPIO26) y azul (GPIO27)

    Args:
        r (bool): True = encender rojo, False = apagar rojo
        v (bool): True = encender verde, False = apagar verde
        a (bool): True = encender azul, False = apagar azul
    """
    # En cátodo común: HIGH en el ánodo = LED ENCENDIDO
    rojo.value(1 if r else 0)  # 1 si queremos encender, 0 si queremos apagar
    verde.value(1 if v else 0)
    azul.value(1 if a else 0)


# ============================================
# SECUENCIA DE COLORES PREDEFINIDOS
# ============================================

# Cada tupla representa (rojo, verde, azul) donde True = encender ese color
colores = [
    (True, False, False),  # 🔴 ROJO
    (False, True, False),  # 🟢 VERDE
    (False, False, True),  # 🔵 AZUL
    (True, True, False),  # 🟡 AMARILLO (rojo + verde)
    (True, False, True),  # 🟣 MAGENTA (rojo + azul)
    (False, True, True),  # 🔵 CIAN (verde + azul)
    (True, True, True),  # ⚪ BLANCO (todos los colores)
    (False, False, False),  # ⚫ APAGADO (ningún color)
]

# Nombres descriptivos para mostrar en consola
nombres = ["ROJO", "VERDE", "AZUL", "AMARILLO", "MAGENTA", "CIAN", "BLANCO", "APAGADO"]


# ============================================
# MENSAJE DE INICIALIZACIÓN
# ============================================
print("=" * 60)
print("🌈 EJEMPLO: Control de LED RGB con ESP32")
print("🎨 Mezcla de luces roja, verde y azul para crear colores")
print("=" * 60)
print("📋 Configuración verificada:")
print("   🔴 GPIO 25 → Ánodo LED Rojo")
print("   🟢 GPIO 26 → Ánodo LED Verde")
print("   🔵 GPIO 27 → Ánodo LED Azul")
print("   ⚫ Cátodo común → GND")
print("   🔧 Cada canal con resistencia 220Ω limitadora")
print("=" * 60)
print("💡 Lógica de cátodo común:")
print("   - GPIO HIGH (3.3V) → ánodo recibiendo voltaje → LED ENCENDIDO")
print("   - GPIO LOW (0V)    → ánodo sin voltaje       → LED APAGADO")
print("=" * 60)
print("🎨 Secuencia de colores que veremos:")
for i, nombre in enumerate(nombres):
    print(f"   {i + 1}. {nombre}")
print("=" * 60)
print("🔁 El ciclo se repetirá continuamente...")
print("💡 Tip: Puedes modificar la lista 'colores' para crear tus propias secuencias!")
print("=" * 60)


# ============================================
# BUCLE PRINCIPAL DE SECUENCIA DE COLORES
# ============================================
indice = 0  # Índice del color actual en la secuencia
while True:
    # OBTENER COLOR ACTUAL DE LA SECUENCIA
    color_actual = colores[indice]  # Tupla (rojo, verde, azul) booleanos

    # APLICAR COLOR AL LED RGB
    establecer_color(*color_actual)  # Desempaqueta la tupla como argumentos

    # MOSTRAR INFORMACIÓN EN CONSOLA
    nombre_color = nombres[indice]
    print(f"💡 Color actual: {nombre_color}")

    # Esperar antes de cambiar al siguiente color
    # 500ms = medio segundo por color (suficiente para apreciar cada uno)
    time.sleep(0.5)

    # AVANZAR AL SIGUIENTE COLOR EN LA SECUENCIA
    # Usamos operador módulo (%) para hacer el índice cíclico
    # Cuando llegamos al final, volvemos al inicio (0)
    indice = (indice + 1) % len(colores)
