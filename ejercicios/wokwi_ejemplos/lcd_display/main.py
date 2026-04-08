"""
Display LCD 16x2 - La Pantalla Clásica de 32 Caracteres
=========================================================

¿QUÉS ES UN LCD?
LCD = "Liquid Crystal Display" (Pantalla de Cristal Líquido).

Es la pantalla que ves en:
• Relojes digitales
• Calculadoras
• Hornos de microondas
• Impresoras
• Instrumentos médicos

El LCD 16x2 significa:
• 16 caracteres por línea
• 2 líneas de texto
• Total: 32 caracteres visibles

Cada carácter está formado por una matriz de 5×8 puntitos (pixels).
Para mostrar una "A", el controlador enciende los pixels específicos.

📚 CÓMO SE COMUNICA (I2C):
─────────────────────────────────────────────────────────────────────────
Antes, los LCD se conectaban con muchos pines (8 bits de datos + 3 de control).
Era un chaos de cables. La solución moderna: un chip PCF8574 que convierte
I2C a esos muchos pines.

  Pico (I2C) → Chip PCF8574 → LCD
    2 cables        8 cables

Esto reduce de 10+ pines a solo 2 (SDA, SCL).

El chip tiene una dirección I2C (0x27 o 0x3F) que depende de cómo
estén configurados los jumpers A0, A1, A2 en el módulo.

📚 CARACTERES ESPECIALES:
─────────────────────────────────────────────────────────────────────────
El LCD tiene caracteres embebidos (built-in):
• Números 0-9
• Letras a-z, A-Z
• Símbolos: ! @ # $ % & *
• Caracteres griegos y japoneses (parcialmente)

Puedes crear CARACTERES PERSONALIZADOS diseñando los 40 pixels (5×8)
y guardándolos en la memoria CG-RAM del LCD.

Se usa en:
• Sistemas de menú
• Mostrar lecturas de sensores
• Relojes y timers
• Interfaces de control

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes: Display LCD 16×2 con módulo I2C (PCF8574)

📌 CONEXIONES FÍSICAS (I2C):
─────────────────────────────────────────────────────────
  Módulo I2C del LCD tiene 4 pines:
    GND → GND (Pico)
    VCC → 5V (Pico VBUS) o 3.3V
    SDA → GPIO 4 (Pico)
    SCL → GPIO 5 (Pico)

  La pantalla LCD en sí tiene 16 pines, pero el módulo I2C los maneja.
  Solo necesitamos los 4 pines del conversor I2C.

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

from machine import Pin, I2C
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN I2C
# ─────────────────────────────────────────────────────────────────────────

# Crear el bus I2C (mismo que el OLED)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# Dirección I2C del LCD (comúnmente 0x27 o 0x3F)
LCD_ADDR = 0x27

# Comandos del HD44780 (controlador del LCD)
LCD_RS = 0x01  # Register Select (comando/dato)
LCD_EN = 0x04  # Enable (activa el dato)
LCD_BACKLIGHT = 0x08  # Retroiluminación
LCD_CLEAR = 0x01  # Limpiar pantalla
LCD_HOME = 0x02  # Cursor a inicio
LCD_LINE1 = 0x80  # Dirección línea 1
LCD_LINE2 = 0xC0  # Dirección línea 2

# Crear objeto para escribir al bus I2C
bus = i2c


def enviar_comando(dato):
    """
    Envía un comando al LCD mediante I2C

    Args:
        dato: Byte de comando (sin datos)

    El LCD funciona con señales de enable (habilitación).
    Enviamos el nibble alto, luego el bajo.
    """
    # Separar en nibbles (4 bits cada uno)
    alto = (dato & 0xF0) | 0x08 | 0x04  # nibble alto + backlight + enable
    bajo = ((dato << 4) & 0xF0) | 0x08  # nibble bajo + backlight (enable bajo)

    # Enviar nibble alto
    bus.writeto(LCD_ADDR, bytes([alto]))
    time.sleep_us(1)
    bus.writeto(LCD_ADDR, bytes([alto & ~0x04]))  # Quitar enable
    time.sleep_us(50)

    # Enviar nibble bajo
    bus.writeto(LCD_ADDR, bytes([bajo]))
    time.sleep_us(1)
    bus.writeto(LCD_ADDR, bytes([bajo & ~0x04]))
    time.sleep_us(50)


def inicializar_lcd():
    """
    Inicializa el LCD en modo 4 bits

    Secuencia necesaria según la hoja de datos del HD44780:
    1. Esperar 50ms (power-on)
    2. Enviar 0x30 tres veces (modo 8 bits)
    3. Cambiar a modo 4 bits
    4. Configurar pantalla (2 líneas, 5x8)
    5. Encender pantalla
    """
    time.sleep_ms(50)  # Esperar a que el LCD arrancque

    # Secuencia de inicialización 8-bit (tres veces)
    enviar_comando(0x30)
    time.sleep_ms(5)
    enviar_comando(0x30)
    time.sleep_us(150)
    enviar_comando(0x30)

    # Cambiar a modo 4 bits
    enviar_comando(0x20)
    enviar_comando(0x20)
    enviar_comando(0xC0)  # 2 líneas, 5x8 caracteres
    enviar_comando(0x10)  # Display on, cursor off
    enviar_comando(0x01)  # Limpiar
    time.sleep_ms(2)


def escribir_lcd(linea, texto):
    """
    Escribe texto en una línea específica del LCD

    Args:
        linea: 0 para primera línea, 1 para segunda línea
        texto: String a mostrar (max 16 caracteres)
    """
    # Posicionar cursor
    if linea == 0:
        enviar_comando(0x80)  # Primera línea
    else:
        enviar_comando(0xC0)  # Segunda línea

    # Escribir cada carácter
    for char in texto:
        # Carácter = datos (RS=1), no comando
        alto = (ord(char) & 0xF0) | 0x08 | 0x04 | 0x01  # RS=1 para datos
        bajo = ((ord(char) << 4) & 0xF0) | 0x08 | 0x01

        bus.writeto(LCD_ADDR, bytes([alto]))
        time.sleep_us(1)
        bus.writeto(LCD_ADDR, bytes([alto & ~0x04]))
        time.sleep_us(50)
        bus.writeto(LCD_ADDR, bytes([bajo]))
        time.sleep_us(1)
        bus.writeto(LCD_ADDR, bytes([bajo & ~0.04]))
        time.sleep_us(50)


def limpiar_lcd():
    """Limpia el contenido del LCD"""
    enviar_comando(0x01)
    time.sleep_ms(2)


# ═══════════════════════════════════════════════════════════════════════════
# PROGRAMA PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("🖥️ INICIANDO: Display LCD 16×2")
print("   Conexión I2C: GPIO 4 (SDA), GPIO 5 (SCL)")
print("   Dirección I2C:", hex(LCD_ADDR))
print("   16 caracteres × 2 líneas")
print("=" * 50)

# Inicializar LCD
time.sleep(1)
inicializar_lcd()
time.sleep(1)

print("✅ LCD inicializado y listo!")

# ═══════════════════════════════════════════════════════════════════════════
# EJEMPLOS DE USO
# ═══════════════════════════════════════════════════════════════════════════

while True:
    # Ejemplo 1: Saludo básico
    print("📝 Ejemplo: Hola Mundo")
    escribir_lcd(0, "Hola Mundo!     ")
    escribir_lcd(1, "MicroPython     ")
    time.sleep(2)

    # Ejemplo 2: Contador en vivo
    print("📝 Ejemplo: Contador")
    for i in range(10):
        escribir_lcd(0, "Contando:      ")
        escribir_lcd(1, f"Numero: {i}       ")
        time.sleep(0.5)

    # Ejemplo 3: Mensaje de bienvenida
    print("📝 Ejemplo: Bienvenida")
    escribir_lcd(0, "Bienvenido!    ")
    escribir_lcd(1, "Al curso Python")
    time.sleep(2)

    # Ejemplo 4: Mensaje motivacional
    print("📝 Ejemplo: Mensaje")
    limpiar_lcd()
    escribir_lcd(0, "Aprende a       ")
    escribir_lcd(1, "programar!      ")
    time.sleep(2)

    # Ejemplo 2: Contador
    for i in range(10):
        escribir_lcd(0, "Contando:      ")
        escribir_lcd(1, f"Numero: {i}       ")
        time.sleep(0.5)

    # Ejemplo 3: Mensajes alternados
    escribir_lcd(0, "Bienvenido!    ")
    escribir_lcd(1, "Al curso Python")
    time.sleep(2)

    limpiar_lcd()
    escribir_lcd(0, "Aprende a       ")
    escribir_lcd(1, "programar!      ")
    time.sleep(2)
