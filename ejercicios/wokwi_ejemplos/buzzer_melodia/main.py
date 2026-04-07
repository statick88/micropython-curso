"""
Buzzer con Melodías - Raspberry Pi Pico
=====================================
Hardware: Raspberry Pi Pico
Componentes: 1 Buzzer piezoeléctrico
Conexionado: GPIO 16 -> Buzzer
Lenguaje: MicroPython
Lógica: Reproduce melodías famosas
"""

from machine import Pin, PWM
import time

# Configuración del buzzer
# GPIO 16 como salida PWM para controlar el tono
buzzer_pin = Pin(16)
buzzer = PWM(buzzer_pin)
buzzer.duty(0)  # Iniciar apagado

# Notas musicales (frecuencias en Hz)
NOTAS = {
    "DO": 261,
    "DO#": 277,
    "RE": 294,
    "RE#": 311,
    "MI": 330,
    "FA": 349,
    "FA#": 370,
    "SOL": 392,
    "SOL#": 415,
    "LA": 440,
    "LA#": 466,
    "SI": 494,
    "DO2": 523,
    "SILENCIO": 0,
}


def tono(frecuencia, duracion=0.3):
    """
    Reproduce un tono específico

    Args:
        frecuencia: Frecuencia en Hz (0 = silencio)
        duracion: Duración en segundos
    """
    if frecuencia == 0:
        buzzer.duty(0)
    else:
        buzzer.freq(frecuencia)
        buzzer.duty(512)  # 50% de ciclo de trabajo
    time.sleep(duracion)
    buzzer.duty(0)  # Apagar entre notas


def nota(nombre, duracion=0.3):
    """Reproduce una nota por nombre"""
    if nombre in NOTAS:
        tono(NOTAS[nombre], duracion)


# Melodías predefinidas
def melodia_navidad():
    """Melodía de Navidad"""
    print("🎄 Melodía de Navidad")
    melodia = [
        ("MI", 0.4),
        ("MI", 0.4),
        ("MI", 0.8),
        ("MI", 0.4),
        ("MI", 0.4),
        ("MI", 0.8),
        ("MI", 0.4),
        ("SOL", 0.4),
        ("DO", 0.4),
        ("RE", 0.4),
        ("MI", 1.0),
        ("RE", 0.8),
        ("RE", 0.8),
        ("RE", 0.4),
        ("RE", 0.4),
        ("RE", 0.4),
        ("MI", 0.4),
        ("MI", 0.4),
        ("MI", 0.4),
        ("MI", 0.4),
        ("MI", 0.4),
        ("MI", 0.4),
        ("SOL", 0.4),
        ("SOL", 0.4),
        ("MI", 0.4),
        ("RE", 0.4),
        ("DO", 0.4),
        ("DO", 0.4),
        ("DO", 0.8),
    ]
    for nota_nombre, duracion in melodia:
        nota(nota_nombre, duracion)
        time.sleep(0.1)


def melodia_cumpleanos():
    """Melodía de Feliz Cumpleaños"""
    print("🎂 Melodía de Cumpleaños")
    melodia = [
        ("DO", 0.4),
        ("DO", 0.4),
        ("RE", 0.4),
        ("DO", 0.4),
        ("FA", 0.4),
        ("MI", 0.8),
        ("DO", 0.4),
        ("DO", 0.4),
        ("RE", 0.4),
        ("DO", 0.4),
        ("SOL", 0.4),
        ("FA", 0.8),
        ("DO", 0.4),
        ("DO", 0.4),
        ("DO2", 0.4),
        ("LA", 0.4),
        ("FA", 0.4),
        ("MI", 0.4),
        ("RE", 0.4),
        ("SI", 0.4),
        ("LA", 0.4),
        ("FA", 0.4),
        ("SOL", 0.4),
        ("RE", 0.8),
    ]
    for nota_nombre, duracion in melodia:
        nota(nota_nombre, duracion)
        time.sleep(0.1)


def melodia_siren():
    """Sonido de sirena"""
    print("🚨 Sirena")
    for _ in range(3):
        # Subir tono
        for freq in range(400, 800, 50):
            tono(freq, 0.05)
        # Bajar tono
        for freq in range(800, 400, -50):
            tono(freq, 0.05)
        time.sleep(0.3)


def melodia_alarma():
    """Sonido de alarma"""
    print("⚠️ Alarma")
    for _ in range(5):
        tono(800, 0.1)
        tono(600, 0.1)
        tono(800, 0.1)
        tono(600, 0.1)
        time.sleep(0.2)


# Mensaje inicial
print("=" * 50)
print("Ejemplo: Buzzer con Melodías")
print("GPIO 16 -> Buzzer piezoeléctrico")
print("=" * 50)

# Bucle principal
while True:
    melodia_navidad()
    time.sleep(1)

    melodia_cumpleanos()
    time.sleep(1)

    melodia_siren()
    time.sleep(1)

    melodia_alarma()
    time.sleep(2)
