/*
  Parpadeo LED - Ejemplo Arduino Básico
  ======================================
  Hardware: Arduino UNO/Nano
  Componentes: 1 LED y 1 resistor de 220Ω
  Conexionado: Pin 13 (LED integrado) o pin 11 (LED externo)
  Lenguaje: Arduino C++
*/

// Configuración del pin LED
const int PIN_LED = 13;  // LED integrado en la mayoría de Arduino

void setup() {
  // Configurar el pin como salida
  pinMode(PIN_LED, OUTPUT);
  
  // Mensaje inicial por puerto serie
  Serial.begin(9600);
  Serial.println("Iniciando ejemplo de parpadeo LED...");
}

void loop() {
  // Encender el LED (HIGH = 5V)
  digitalWrite(PIN_LED, HIGH);
  Serial.println("LED ENCENDIDO");
  delay(1000);  // Esperar 1 segundo

  // Apagar el LED (LOW = 0V)
  digitalWrite(PIN_LED, LOW);
  Serial.println("LED APAGADO");
  delay(1000);  // Esperar 1 segundo
}
