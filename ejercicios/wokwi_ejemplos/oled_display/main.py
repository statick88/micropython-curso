"""
Display OLED SSD1306 - Ejemplo de Salida Gráfica I2C
==================================================
Hardware: Raspberry Pi Pico con MicroPython
Componentes: 1 display OLED SSD1306 (128x64 pixels)
Conexionado: I2C0 - SDA=GPIO4, SCL=GPIO5
Lenguaje: MicroPython con librería ssd1306
Lógica: Muestra texto, figuras y animaciones básicas
"""

from machine import Pin, I2C
import ssd1306
import time

# Configuración del bus I2C
# I2C(0) usa GPIO4 (SDA) y GPIO5 (SCL) por defecto
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# Buscar la dirección del display OLED
print("Direcciones I2C encontradas:", hex(i2c.scan()))

# Inicializar el display OLED (128x64)
# SSD1306_I2C_ADDRESS = 0x3C (dirección común)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Colores disponibles
NEGRO = 0
BLANCO = 1


def limpiar_pantalla():
    """Limpia el contenido del display"""
    oled.fill(NEGRO)
    oled.show()


def mostrar_texto(x, y, texto):
    """
    Muestra texto en el display

    Args:
        x: Posición horizontal (0-127)
        y: Posición vertical (0-57)
        texto: String a mostrar
    """
    oled.text(texto, x, y)
    oled.show()


def dibujar_rectangulo(x1, y1, x2, y2, color=BLANCO):
    """
    Dibuja un rectángulo en el display

    Args:
        x1, y1: Esquina superior izquierda
        x2, y2: Esquina inferior derecha
        color: Color de relleno (opcional)
    """
    oled.rect(x1, y1, x2 - x1, y2 - y1, color)
    oled.show()


def dibujar_linea(x1, y1, x2, y2):
    """
    Dibuja una línea en el display

    Args:
        x1, y1: Punto inicial
        x2, y2: Punto final
    """
    oled.line(x1, y1, x2, y2, BLANCO)
    oled.show()


def ejemplo_texto_basico():
    """Ejemplo 1: Texto básico"""
    print("Ejemplo 1: Texto básico")
    oled.fill(NEGRO)
    oled.text("Hola Mundo!", 20, 20)
    oled.text("MicroPython", 25, 35)
    oled.text("en Wokwi", 30, 50)
    oled.show()
    time.sleep(3)


def ejemplo_formas():
    """Ejemplo 2: Formas geométricas"""
    print("Ejemplo 2: Formas geométricas")
    oled.fill(NEGRO)

    # Dibujar un rectángulo
    oled.rect(10, 10, 30, 20, BLANCO)

    # Dibujar un círculo (solo pixel más cercano)
    oled.circle(80, 30, 15, BLANCO)

    # Dibujar líneas
    oled.line(0, 0, 127, 63, BLANCO)
    oled.line(0, 63, 127, 0, BLANCO)

    oled.show()
    time.sleep(3)


def ejemplo_contador():
    """Ejemplo 3: Contador ascendente"""
    print("Ejemplo 3: Contador")
    for i in range(20):
        oled.fill(NEGRO)
        oled.text("Contador:", 30, 20)
        oled.text(str(i), 50, 40)
        oled.show()
        time.sleep(0.2)


def ejemplo_barra_progreso(valor, maximo):
    """
    Dibuja una barra de progreso

    Args:
        valor: Valor actual
        maximo: Valor máximo
    """
    oled.fill(NEGRO)
    oled.text("Progreso:", 30, 10)

    # Calcular ancho de la barra
    ancho = int((valor / maximo) * 108)

    # Dibujar fondo de la barra
    oled.rect(10, 30, 108, 20, BLANCO)
    # Dibujar relleno
    oled.fill_rect(12, 32, max(0, ancho - 4), 16, BLANCO)

    # Mostrar porcentaje
    porcentaje = int((valor / maximo) * 100)
    oled.text(f"{porcentaje}%", 50, 55)

    oled.show()


def ejemplo_barra_progreso_completa():
    """Ejemplo de barra de progreso animada"""
    print("Ejemplo: Barra de progreso")
    for i in range(101):
        ejemplo_barra_progreso(i, 100)
        time.sleep(0.05)


def ejemplo_animacion_pixel():
    """Ejemplo de animación de pixel móvil"""
    print("Ejemplo: Animación de pixel")
    x = 0
    direccion = 1

    for _ in range(100):
        oled.fill(NEGRO)
        oled.pixel(x, 32, BLANCO)
        oled.show()

        x += direccion
        if x > 127 or x < 0:
            direccion *= -1

        time.sleep(0.03)


# Programa principal
print("Iniciando ejemplos de OLED SSD1306...")
time.sleep(1)

# Ejecutar todos los ejemplos
while True:
    ejemplo_texto_basico()
    ejemplo_formas()
    ejemplo_contador()
    ejemplo_barra_progreso_completa()
    ejemplo_animacion_pixel()
