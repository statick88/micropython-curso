"""
Buzzer Piezoeléctrico - Tu Primer Instrumento Musical
====================================================

¿QUÉS ES ESTO?
Un buzzer piezoeléctrico es como un pequeño altavoz que puede producir tonos y melodías al recibir señales eléctricas. Es perfecto para crear alarmas, tocar canciones simples o dar feedback sonoro en tus proyectos.

Hardware: Raspberry Pi Pico con MicroPython
Plataforma: Wokwi
Componentes: Buzzer piezoeléctrico

📌 CONEXIONES FÍSICAS (2 cables):
─────────────────────────────────────────────────────────
   GPIO 16 (Pico) ──────► Terminal (+) del buzzer
   GND (Pico) ──────────► Terminal (-) del buzzer

   ⚠️ OJO: Los buzzers tienen polaridad. El terminal (+) suele tener
   un signo (+) marcado, o es el más largo de los dos cables.

Lenguaje: MicroPython
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXPLICACIÓN DEL CÓDIGO
# ═══════════════════════════════════════════════════════════════════════════

from machine import Pin, PWM
import time

# ─────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DEL BUZZER
# ─────────────────────────────────────────────────────────────────────────
# Usamos PWM para crear diferentes frecuencias (tonos)
# PWM nos permite variar la frecuencia del sonido
buzzer_pin = Pin(16)
buzzer = PWM(buzzer_pin)
buzzer.duty(0)  # Iniciar en silencio (sin sonido)

# Diccionario de notas musicales con sus frecuencias
# Estas son las notas de la octava central (la que comúnmente usamos)
NOTAS = {
    "DO": 261,  # C4
    "DO#": 277,  # C#4
    "RE": 294,  # D4
    "RE#": 311,  # D#4
    "MI": 330,  # E4
    "FA": 349,  # F4
    "FA#": 370,  # F#4
    "SOL": 392,  # G4
    "SOL#": 415,  # G#4
    "LA": 440,  # A4 (nota de afinación)
    "LA#": 466,  # A#4
    "SI": 494,  # B4
    "DO2": 523,  # C5 (una octava más alta)
    "SILENCIO": 0,  # Sin sonido
}


def tono(frecuencia, duracion=0.3):
    """
    Reproduce un tono a una frecuencia específica

    Args:
        frecuencia: Frecuencia en Hz (0 = silencio)
        duracion: Cuánto dura el tono en segundos
    """
    if frecuencia == 0:
        # Silencio: apagar el buzzer
        buzzer.duty(0)
    else:
        # Configurar la frecuencia del tono
        buzzer.freq(frecuencia)
        # duty(512) ≈ 50% - volumen medio
        buzzer.duty(512)

    # Mantener el tono por la duración especificada
    time.sleep(duracion)

    # Apagar entre notas para que suenen separadas
    buzzer.duty(0)


def nota(nombre_nota, duracion=0.3):
    """
    Reproduce una nota por su nombre

    Args:
        nombre_nota: Nombre de la nota (ej: "DO", "MI", "SOL")
        duracion: Duración en segundos
    """
    if nombre_nota in NOTAS:
        tono(NOTAS[nombre_nota], duracion)
    else:
        # Si la nota no existe, silencio
        tono(0, duracion)


# ═══════════════════════════════════════════════════════════════════════════
# MELODÍAS PREDEFINIDAS
# ═══════════════════════════════════════════════════════════════════════════


def melodia_navidad():
    """🎄 Reproduce la conocida melodía de Navidad (Jingle Bells)"""
    print("🎄 Tocando: Jingle Bells")
    # Notas de la canción famosa
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
        ("RE", 0.4),
        ("DO", 0.4),
        ("DO", 0.4),
    ]
    for nombre, dur in melodia:
        nota(nombre, dur)
        time.sleep(0.1)  # Pausa entre notas


def melodia_cumpleanos():
    """🎂 Reproduce la canción de Feliz Cumpleaños"""
    print("🎂 Tocando: Feliz Cumpleaños")
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
    ]
    for nombre, dur in melodia:
        nota(nombre, dur)
        time.sleep(0.1)


def melodia_siren():
    """🚨 Reproduce un sonido de sirena"""
    print("🚨 Efecto: Sirena de policía")
    for _ in range(3):
        # Frecuencia creciente (como subiendo)
        for freq in range(400, 800, 50):
            tono(freq, 0.05)
        # Frecuencia decreciente (como bajando)
        for freq in range(800, 400, -50):
            tono(freq, 0.05)
        time.sleep(0.3)


def melodia_alarma():
    """⚠️ Reproduce sonido de alarma"""
    print("⚠️ Efecto: Alarma")
    for _ in range(5):
        tono(800, 0.1)  # Beep agudo
        tono(600, 0.1)  # Beep grave
    time.sleep(0.2)


# ═══════════════════════════════════════════════════════════════════════════
# PROGRAMA PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

print("🔊 INICIANDO: Buzzer Piezoeléctrico")
print("   Pin GPIO 16 -> Buzzer")
print("   ¡Escucharás diferentes melodías!")
print("=" * 50)

# Bucle principal: reproducir melodías una tras otra
while True:
    melodia_navidad()
    time.sleep(1)

    melodia_cumpleanos()
    time.sleep(1)

    melodia_siren()
    time.sleep(1)

    melodia_alarma()
    time.sleep(2)
