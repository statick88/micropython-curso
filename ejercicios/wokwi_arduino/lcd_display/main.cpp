/*
  Display LCD 16x2 - Arduino I2C
  ==============================
  Hardware: Arduino UNO/Nano
  Componentes: Display LCD 1602 con módulo I2C
  Conexionado: I2C - SDA=A4, SCL=A5
  Librería: LiquidCrystal I2C ( Frank de Vries )
*/

#include <LiquidCrystal_I2C.h>

// Inicializar LCD (dirección 0x27, 16 columnas, 2 filas)
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  // Iniciar LCD
  lcd.init();
  lcd.backlight();
  
  Serial.begin(9600);
  Serial.println("LCD iniciado");
  
  // Mensaje inicial
  lcd.print("Hola Mundo!");
  Serial.println("Hola Mundo!");
  delay(2000);
}

void mostrarContador() {
  for(int i = 0; i <= 20; i++) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Contador:");
    lcd.setCursor(0, 1);
    lcd.print(i);
    
    Serial.print("Contador: ");
    Serial.println(i);
    delay(500);
  }
}

void mostrarTextoDeslizante() {
  String texto = "MicroPython en Arduino - Curso ";
  int longitud = texto.length();
  
  for(int pos = 0; pos <= longitud - 16; pos++) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(texto.substring(pos, pos + 16));
    delay(300);
  }
}

void mostrarSensor() {
  // Simular lectura de sensor
  for(int i = 0; i < 5; i++) {
    int valor = analogRead(A0);
    float temperatura = valor * 0.48828125; // Convertir a temperatura
    
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Temperatura:");
    lcd.setCursor(0, 1);
    lcd.print(temperatura);
    lcd.print(" C");
    
    Serial.print("Temperatura: ");
    Serial.print(temperatura);
    Serial.println(" C");
    
    delay(1000);
  }
}

void loop() {
  mostrarContador();
  mostrarTextoDeslizante();
  mostrarSensor();
}
