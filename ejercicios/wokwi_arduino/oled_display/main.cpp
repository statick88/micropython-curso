/*
  Display OLED SSD1306 - Arduino I2C
  ==================================
  Hardware: Arduino UNO/Nano
  Componentes: Display OLED SSD1306 128x64
  Conexionado: I2C - SDA=A4, SCL=A5
  Librería: Adafruit SSD1306 (instalar desde Library Manager)
*/

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// Configuración OLED
#define ANCHO_PANTALLA 128
#define ALTO_PANTALLA 64

// Inicializar display (I2C address 0x3C)
Adafruit_SSD1306 pantalla(ANCHO_PANTALLA, ALTO_PANTALLA, &Wire, -1);

void setup() {
  Serial.begin(9600);
  
  // Iniciar OLED
  if(!pantalla.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("Error: OLED no encontrado");
    while(true);
  }
  
  // Limpiar pantalla
  pantalla.clearDisplay();
  pantalla.display();
  
  Serial.println("OLED iniciado correctamente");
}

void mostrarTexto() {
  pantalla.clearDisplay();
  pantalla.setTextSize(2);
  pantalla.setTextColor(SSD1306_WHITE);
  pantalla.setCursor(10, 10);
  pantalla.println("Hola");
  pantalla.setCursor(10, 35);
  pantalla.println("Mundo!");
  pantalla.display();
  delay(2000);
}

void mostrarContador() {
  for(int i = 0; i < 20; i++) {
    pantalla.clearDisplay();
    pantalla.setTextSize(3);
    pantalla.setTextColor(SSD1306_WHITE);
    pantalla.setCursor(40, 25);
    pantalla.println(i);
    pantalla.display();
    delay(200);
  }
}

void mostrarBarraProgreso() {
  for(int prog = 0; prog <= 100; prog += 5) {
    pantalla.clearDisplay();
    pantalla.setTextSize(1);
    pantalla.setCursor(0, 0);
    pantalla.println("Progreso:");
    
    // Barra
    pantalla.drawRect(10, 20, 108, 20, SSD1306_WHITE);
    pantalla.fillRect(12, 22, map(prog, 0, 100, 0, 104), 16, SSD1306_WHITE);
    
    // Porcentaje
    pantalla.setCursor(50, 50);
    pantalla.print(prog);
    pantalla.println("%");
    
    pantalla.display();
    delay(50);
  }
}

void mostrarFormas() {
  pantalla.clearDisplay();
  
  // Línea
  pantalla.drawLine(0, 0, 127, 63, SSD1306_WHITE);
  
  // Rectángulo
  pantalla.drawRect(10, 10, 30, 20, SSD1306_WHITE);
  
  // Círculo
  pantalla.drawCircle(80, 40, 15, SSD1306_WHITE);
  
  // Triángulo
  pantalla.drawTriangle(100, 10, 110, 30, 90, 30, SSD1306_WHITE);
  
  pantalla.display();
  delay(3000);
}

void loop() {
  mostrarTexto();
  mostrarContador();
  mostrarBarraProgreso();
  mostrarFormas();
}
