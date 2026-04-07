"""
Display LCD 16x2 - Raspberry Pi Pico
====================================
Hardware: Raspberry Pi Pico
Componentes: 1 Display LCD 16x2 con backlight
Conexionado: I2C0 - GPIO 4 (SDA), GPIO 5 (SCL)
Lenguaje: MicroPython
Lógica: Muestra mensajes en el LCD
"""

from machine import Pin, I2C
import time

# Configuración I2C para LCD
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# Dirección típica del LCD (0x27 o 0x3F)
LCD_ADDR = 0x27

# Comandos del LCD
LCD_RS = 0x01
LCD_EN = 0x04
LCD_BACKLIGHT = 0x08
LCD_CLEAR = 0x01
LCD_HOME = 0x02
LCD_LINE1 = 0x80
LCD_LINE2 = 0xC0

def lcd_write nibble, char_mode=0):
    """Escribe un nibble en el LCD"""
    # Alto
    bus.write_byte(LCD_ADDR, nibble | char_mode | LCD_BACKLIGHT | LCD_EN)
    time.sleep_us(1)
    bus.write_byte(LCD_ADDR, nibble | char_mode | LCD_BACKLIGHT)
    time.sleep_us(50)

def lcd_char(char):
    """Escribe un carácter en el LCD"""
    char_mode = 0x01  # Datos
    alto = char & 0xF0
    bajo = (char << 4) & 0xF0
    lcd_write(alto, char_mode)
    lcd_write(bajo, char_mode)

def lcd_command cmd):
    """Envia un comando al LCD"""
    char_mode = 0x00  # Comando
    alto = cmd & 0xF0
    bajo = (cmd << 4) & 0xF0
    lcd_write(alto, char_mode)
    lcd_write(bajo, char_mode)

def lcd_init():
    """Inicializa el LCD"""
    from machine import I2C as I2C_bus
    bus = I2C_bus(0, scl=Pin(5), sda=Pin(4))
    global bus
    time.sleep_ms(50)
    lcd_write(0x30)
    time.sleep_ms(5)
    lcd_write(0x30)
    time.sleep_us(150)
    lcd_write(0x30)
    lcd_write(0x20)
    lcd_write(0x20)
    lcd_write(0xC0)
    lcd_write(0x10)
    lcd_write(0x01)
    time.sleep_ms(3)

def lcd_clear():
    """Limpia el LCD"""
    lcd_command(LCD_CLEAR)
    time.sleep_ms(2)

def lcd_set_cursor(line, col):
    """Posiciona el cursor"""
    if line == 0:
        lcd_command(LCD_LINE1 + col)
    else:
        lcd_command(LCD_LINE2 + col)

def lcd_print(text):
    """Imprime texto en la posición actual"""
    for char in text:
        lcd_char(ord(char))

# Versión simplificada usando la librería I2C
from machine import I2C as I2C_bus
bus = I2C(0, scl=Pin(5), sda=Pin(4))

def inicializar_lcd():
    """Inicialización del LCD 16x2"""
    time.sleep_ms(50)
    # Secuencia de inicialización
    enviar_comando(0x30)
    time.sleep_ms(5)
    enviar_comando(0x30)
    time.sleep_us(150)
    enviar_comando(0x30)
    enviar_comando(0x20)
    enviar_comando(0x20)
    enviar_comando(0xC0)
    enviar_comando(0x10)
    enviar_comando(0x01)
    time.sleep_ms(2)

def enviar_comando(dato):
    """Envía un comando al LCD"""
    alto = (dato & 0xF0) | 0x08 | 0x04
    bajo = ((dato << 4) & 0xF0) | 0x08
    bus.writeto(LCD_ADDR, bytes([alto]))
    time.sleep_us(1)
    bus.writeto(LCD_ADDR, bytes([alto & ~0x04]))
    time.sleep_us(50)
    bus.writeto(LCD_ADDR, bytes([bajo]))
    time.sleep_us(1)
    bus.writeto(LCD_ADDR, bytes([bajo & ~0x04]))
    time.sleep_us(50)

def escribir_lcd(linea, texto):
    """Escribe texto en una línea específica"""
    if linea == 0:
        enviar_comando(0x80)  # Primera línea
    else:
        enviar_comando(0xC0)  # Segunda línea
    for char in texto:
        alto = (ord(char) & 0xF0) | 0x08 | 0x04 | 0x01
        bajo = ((ord(char) << 4) & 0xF0) | 0x08 | 0x01
        bus.writeto(LCD_ADDR, bytes([alto]))
        bus.writeto(LCD_ADDR, bytes([alto & ~0x04]))
        time.sleep_us(50)
        bus.writeto(LCD_ADDR, bytes([bajo]))
        bus.writeto(LCD_ADDR, bytes([bajo & ~0x04]))
        time.sleep_us(50)

def limpiar_lcd():
    """Limpia el LCD"""
    enviar_comando(0x01)
    time.sleep_ms(2)

# Programa principal
print("=" * 50)
print("Display LCD 16x2")
print("I2C: GPIO 4 (SDA), GPIO 5 (SCL)")
print("=" * 50)

time.sleep(1)
inicializar_lcd()
time.sleep(1)

# Ejemplos de texto
while True:
    # Ejemplo 1: Hola Mundo
    escribir_lcd(0, "Hola Mundo!     ")
    escribir_lcd(1, "MicroPython     ")
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