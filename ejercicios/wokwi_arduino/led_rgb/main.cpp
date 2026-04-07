/*
  Control LED RGB - Ejemplo Arduino
  =================================
  Hardware: Arduino UNO/Nano
  Componentes: 1 LED RGB (ánodo común) y 3 resistores de 220Ω
  Conexionado: Pin 11 -> Rojo, Pin 10 -> Verde, Pin 9 -> Azul
  Lenguaje: Arduino C++
*/

// Pines para LED RGB
const int PIN_ROJO = 11;
const int PIN_VERDE = 10;
const int PIN_AZUL = 9;

void setup() {
  // Configurar pines como salida
  pinMode(PIN_ROJO, OUTPUT);
  pinMode(PIN_VERDE, OUTPUT);
  pinMode(PIN_AZUL, OUTPUT);
  
  // Iniciar con LED apagado
  digitalWrite(PIN_ROJO, LOW);
  digitalWrite(PIN_VERDE, LOW);
  digitalWrite(PIN_AZUL, LOW);
  
  Serial.begin(9600);
  Serial.println("Iniciando ejemplo LED RGB...");
}

void setColor(bool r, bool v, bool a) {
  // Para ánodo común: LOW = LED encendido
  digitalWrite(PIN_ROJO, !r);
  digitalWrite(PIN_VERDE, !v);
  digitalWrite(PIN_AZUL, !a);
}

void loop() {
  // Secuencia de colores
  setColor(true, false, false);  // Rojo
  Serial.println("ROJO");
  delay(500);
  
  setColor(false, true, false);  // Verde
  Serial.println("VERDE");
  delay(500);
  
  setColor(false, false, true);   // Azul
  Serial.println("AZUL");
  delay(500);
  
  setColor(true, true, false);    // Amarillo
  Serial.println("AMARILLO");
  delay(500);
  
  setColor(true, false, true);    // Magenta
  Serial.println("MAGENTA");
  delay(500);
  
  setColor(false, true, true);    // Cian
  Serial.println("CIAN");
  delay(500);
  
  setColor(true, true, true);     // Blanco
  Serial.println("BLANCO");
  delay(500);
  
  setColor(false, false, false);  // Apagado
  Serial.println("APAGADO");
  delay(500);
}
