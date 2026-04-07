# Simulación del Hub en tu computadora
# (No controla un robot real, pero puedes practicar la lógica)

class FakeHub:
    """Simula las funciones del Hub LEGO"""
    
    def __init__(self):
        self.pantalla = ""
        self.luz = "apagada"
    
    def display_text(self, mensaje):
        print(f"📺 PANTALLA: {mensaje}")
        self.pantalla = mensaje
    
    def light_on(self, color):
        colores = {0: "rojo", 5: "verde", 10: "amarillo", 3: "azul"}
        print(f"🔵 LED: Color {colores.get(color, 'desconocido')}")
        self.luz = "encendida"
    
    def light_off(self):
        print("🔴 LED: Apagado")
        self.luz = "apagada"
    
    def speaker_beep(self):
        print("🔊 BEEP!")
    
    @property
    def button(self):
        return FakeButton()

class FakeButton:
    def pressed(self):
        return False

# USAR COMO SI FUERA EL HUB REAL
hub = FakeHub()
hub.display_text("Esto es una practica con un fake hub")
hub.light_on(5)
hub.speaker_beep()