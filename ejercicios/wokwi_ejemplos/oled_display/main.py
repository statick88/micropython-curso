"""
Display OLED SSD1306 - Tu Pantalla Pequeña pero Potente
=====================================================

¿QUÉS ES ESTO?
El display OLED SSD1306 es una pantalla pequeña pero poderosa que nos permite
mostrar texto, gráficos y animaciones en tiempo real. A diferencia de las
pantallas tradicionales, cada píxel genera su propia luz, lo que da negros
profundos y contraste excelente.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes: Display OLED SSD1306 (128×64 pixeles)

📌 CONEXIONES FÍSICAS (I2C):
─────────────────────────────────────────────────────────
   El OLED tiene 4 pines:
     GND → GND (Pico)
     VCC → 3.3V (Pico)
     SDA → GPIO 4 (Pico) - línea de datos
     SCL → GPIO 5 (Pico) - línea de reloj

   En Wokwi, el componente ya tiene la configuración lista.
   Solo definimos: I2C(0) con scl=Pin(5), sda=Pin(4)

Lenguaje: MicroPython (con librería ssd1306)
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

from machine import Pin, I2C
import ssd1306
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN I2C Y OLED
# ─────────────────────────────────────────────────────────────────────────

# Crear el bus I2C
# I2C(0) usa pines por defecto: SDA=GPIO4, SCL=GPIO5
# freq=400000 = 400kHz (velocidad rápida)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# Escanear el bus para encontrar dispositivos
print("🔍 Buscando dispositivos I2C...")
direcciones = i2c.scan()
print(f"   Dispositivos encontrados: {[hex(d) for d in direcciones]}")

# Crear el objeto del display OLED
# 128 = ancho en pixeles, 64 = alto en pixeles
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Definir colores (en OLED solo hay 2)
NEGRO = 0  # Pixel apagado
BLANCO = 1  # Pixel encendido


# ═══════════════════════════════════════════════════════════════════════════
# FUNCIONES AUXILIARES
# ═══════════════════════════════════════════════════════════════════════════


def limpiar_pantalla():
    """Borra todo el contenido de la pantalla"""
    oled.fill(NEGRO)
    oled.show()


def mostrar_texto(x, y, texto):
    """
    Muestra texto en coordenadas específicas

    Args:
        x: Posición horizontal (0 a 127)
        y: Posición vertical (0 a 57, en saltos de 8)
        texto: String a mostrar
    """
    oled.text(texto, x, y)
    oled.show()


def dibujar_rectangulo(x1, y1, x2, y2, color=BLANCO):
    """
    Dibuja un rectángulo entre dos puntos

    Args:
        x1, y1: Esquina superior izquierda
        x2, y2: Esquina inferior derecha
        color: 0 = vacío, 1 = lleno
    """
    oled.rect(x1, y1, x2 - x1, y2 - y1, color)
    oled.show()


def dibujar_linea(x1, y1, x2, y2):
    """
    Dibuja una línea entre dos puntos

    Args:
        x1, y1: Punto inicial
        x2, y2: Punto final
    """
    oled.line(x1, y1, x2, y2, BLANCO)
    oled.show()


# ═══════════════════════════════════════════════════════════════════════════
# EJEMPLOS DE USO
# ═══════════════════════════════════════════════════════════════════════════


def ejemplo_texto_basico():
    """📝 Ejemplo 1: Mostrar texto simple"""
    print("📝 Ejemplo: Texto básico")
    oled.fill(NEGRO)  # Limpiar
    oled.text("Hola Mundo!", 20, 20)
    oled.text("MicroPython", 25, 35)
    oled.text("en Wokwi", 30, 50)
    oled.show()
    time.sleep(3)


def ejemplo_formas():
    """⬜ Ejemplo 2: Dibujar formas geométricas"""
    print("⬜ Ejemplo: Formas geométricas")
    oled.fill(NEGRO)

    # Rectángulo (x, y, ancho, alto, color)
    oled.rect(10, 10, 30, 20, BLANCO)

    # Círculo (centro_x, centro_y, radio, color)
    oled.circle(80, 30, 15, BLANCO)

    # Líneas cruzadas (efecto X)
    oled.line(0, 0, 127, 63, BLANCO)
    oled.line(0, 63, 127, 0, BLANCO)

    oled.show()
    time.sleep(3)


def ejemplo_contador():
    """🔢 Ejemplo 3: Contador ascendente"""
    print("🔢 Ejemplo: Contador")
    for i in range(20):
        oled.fill(NEGRO)
        oled.text("Contador:", 30, 20)
        oled.text(str(i), 50, 40)  # Mostrar número
        oled.show()
        time.sleep(0.2)


def ejemplo_barra_progreso(valor, maximo):
    """
    📊 Ejemplo 4: Barra de progreso

    Args:
        valor: Valor actual (0 a maximo)
        maximo: Valor máximo (para calcular porcentaje)
    """
    oled.fill(NEGRO)
    oled.text("Progreso:", 30, 10)

    # Calcular ancho de la barra (108 pixeles máximo)
    ancho = int((valor / maximo) * 108)

    # Marco de la barra
    oled.rect(10, 30, 108, 20, BLANCO)
    # Relleno de la barra
    oled.fill_rect(12, 32, max(0, ancho - 4), 16, BLANCO)

    # Porcentaje como texto
    porcentaje = int((valor / maximo) * 100)
    oled.text(f"{porcentaje}%", 50, 55)

    oled.show()


def ejemplo_barra_progreso_completa():
    """Barra de progreso animada"""
    print("📊 Ejemplo: Barra de progreso")
    for i in range(101):
        ejemplo_barra_progreso(i, 100)
        time.sleep(0.05)


def ejemplo_animacion_pixel():
    """🔵 Ejemplo de animación: pixel rebotando"""
    print("🔵 Ejemplo: Animación de pixel")
    x = 0  # Posición inicial
    direccion = 1  # 1 = derecha, -1 = izquierda

    for _ in range(100):
        oled.fill(NEGRO)
        oled.pixel(x, 32, BLANCO)  # Un solo pixel
        oled.show()

        # Mover el pixel
        x += direccion

        # Rebotar en los bordes
        if x > 127 or x < 0:
            direccion *= -1

        time.sleep(0.03)


# ═══════════════════════════════════════════════════════════════════════════
# PROGRAMA PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("🖥️ INICIANDO: Display OLED SSD1306")
print("   Conexión I2C: GPIO 4 (SDA), GPIO 5 (SCL)")
print("   Resolución: 128 × 64 pixeles")
print("=" * 50)

time.sleep(1)

# Ejecutar todos los ejemplos en loop
while True:
    ejemplo_texto_basico()
    ejemplo_formas()
    ejemplo_contador()
    ejemplo_barra_progreso_completa()
    ejemplo_animacion_pixel()
