"""
Display LCD 16x2 - ESP32
=======================
Hardware: ESP32 DevKit V1
Componentes: 1 Display LCD 16x2
Conexionado: I2C1 - GPIO 21 (SDA), GPIO 22 (SCL)
Lenguaje: MicroPython
Lógica: Muestra mensajes en el LCD
"""

from machine import Pin, I2C
import time

# Configuración I2C para LCD (usando I2C1 en ESP32)
i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=400000)

LCD_ADDR = 0x27


def enviar_nibble(dato, modo=0):
    """Envía un nibble al LCD"""
    enable = 0x04
    alto = (dato & 0xF0) | 0x08 | enable | modo
    bajo = ((dato << 4) & 0xF0) | 0x08 | enable | modo

    i2c.writeto(LCD_ADDR, bytes([alto]))
    time.sleep_us(1)
    i2c.writeto(LCD_ADDR, bytes([alto & ~enable]))
    time.sleep_us(50)
    i2c.writeto(LCD_ADDR, bytes([bajo]))
    time.sleep_us(1)
    i2c.writeto(LCD_ADDR, bytes([bajo & ~enable]))
    time.sleep_us(50)


def comando(dato):
    """Envía un comando al LCD"""
    enviar_nibble(dato, 0)


def dato_lcd(caracter):
    """Envía un dato al LCD"""
    enviar_nibble(caracter, 1)


def inicializar_lcd():
    """Inicializa el LCD"""
    time.sleep_ms(50)
    comando(0x30)
    time.sleep_ms(5)
    comando(0x30)
    time.sleep_us(150)
    comando(0x30)
    comando(0x20)
    comando(0x20)
    comando(0xC0)
    comando(0x10)
    comando(0x01)
    time.sleep_ms(2)


def escribir(linea, texto):
    """Escribe en una línea específica"""
    if linea == 0:
        comando(0x80)
    else:
        comando(0xC0)
    for char in texto:
        dato_lcd(ord(char))
        time.sleep_us(50)


def limpiar():
    """Limpia el LCD"""
    comando(0x01)
    time.sleep_ms(2)


# Programa principal
print("=" * 50)
print("Display LCD 16x2 - ESP32")
print("I2C1: GPIO 21 (SDA), GPIO 22 (SCL)")
print("=" * 50)

time.sleep(1)
inicializar_lcd()

while True:
    escribir(0, "Hola Mundo!    ")
    escribir(1, "ESP32 + Python")
    time.sleep(2)

    for i in range(10):
        escribir(0, "Contando:     ")
        escribir(1, f"Num: {i}          ")
        time.sleep(0.5)

    escribir(0, "Aprende Python!")
    escribir(1, "Con Wokwi      ")
    time.sleep(2)
