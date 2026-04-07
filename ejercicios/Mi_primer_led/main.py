from machine import Pin #Se importa el Pin
from time import sleep #Se agrega tiempo

ledRed = Pin(19, Pin.OUT) # Se agrega el pin 19
ledGreen = Pin(18, Pin.OUT) # Se agrega el pin 18

while True:
    ledRed.value(1) #Led Rojo se enciende
    print("LED Red PRENDIDO!")
    sleep(1) # Espera un segundo
    
    ledRed.value(0) #Led Rojo se apaga
    print("LED Red APAGADO")
    sleep(1) # Espera un segundo
    
    # Ahora el led green

    ledGreen.value(1)
    print("Led Green Encendido")
    sleep(1)

    ledGreen.value(0)
    print("Led Green Apagado")
    sleep(2)