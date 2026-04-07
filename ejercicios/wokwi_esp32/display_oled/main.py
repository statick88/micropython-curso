"""
Display OLED SSD1306 - ESP32 con MicroPython
===========================================
Hardware: ESP32 DevKit V1
Componentes: 1 display OLED SSD1306 (128x64 pixels)
Conexionado: I2C0 - SDA=GPIO21, SCL=GPIO22
Lenguaje: MicroPython con librería ssd1306
Lógica: Muestra texto, figuras y animaciones básicas
"""

from machine import Pin, I2C
import ssd1306
import time

# Configuración del bus I2C para ESP32
# I2C(0) usa GPIO 21 (SDA) y GPIO 22 (SCL)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

# Buscar la dirección del display OLED
print("=" * 50)
print("Ejemplo: Display OLED SSD1306 con ESP32")
print("I2C: GPIO 21 (SDA), GPIO 22 (SCL)")
print("=" * 50)
print("Direcciones I2C encontradas:", [hex(x) for x in i2c.scan()])

# Inicializar el display OLED (128x64)
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


def ejemplo_texto_basico():
    """Ejemplo 1: Texto básico"""
    print("Ejemplo 1: Texto básico")
    oled.fill(NEGRO)
    oled.text("Hola Mundo!", 20, 15)
    oled.text("ESP32 + MicroPython", 5, 30)
    oled.text("en Wokwi", 30, 45)
    oled.show()
    time.sleep(3)


def ejemplo_formas():
    """Ejemplo 2: Formas geométricas"""
    print("Ejemplo 2: Formas geométricas")
    oled.fill(NEGRO)

    # Dibujar un rectángulo
    oled.rect(10, 10, 30, 20, BLANCO)

    # Dibujar un círculo
    oled.circle(80, 30, 15, BLANCO)

    # Dibujar líneas cruzadas
    oled.line(0, 0, 127, 63, BLANCO)
    oled.line(0, 63, 127, 0, BLANCO)

    oled.show()
    time.sleep(3)


def ejemplo_contador():
    """Ejemplo 3: Contador ascendente"""
    print("Ejemplo 3: Contador")
    for i in range(20):
        oled.fill(NEGRO)
        oled.text("Contador:", 30, 15)
        oled.text(str(i), 50, 35)
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

    # Calcular ancho de la barra (108 pixeles disponibles)
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
        time.sleep(0.03)


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

# Ejecutar todos los ejemplos en bucle
while True:
    ejemplo_texto_basico()
    ejemplo_formas()
    ejemplo_contador()
    ejemplo_barra_progreso_completa()
    ejemplo_animacion_pixel()
