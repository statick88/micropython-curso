/*
  Sensor de Distancia HC-SR04 - Arduino
  =====================================
  Hardware: Arduino UNO/Nano
  Componentes: Sensor ultrasónico HC-SR04
  Conexionado: Pin 9 -> Trigger, Pin 10 -> Echo
  Lenguaje: Arduino C++
*/

const int PIN_TRIGGER = 9;
const int PIN_ECHO = 10;

void setup() {
  pinMode(PIN_TRIGGER, OUTPUT);
  pinMode(PIN_ECHO, INPUT);
  
  Serial.begin(9600);
  Serial.println("Sensor de distancia HC-SR04");
}

long medirDistancia() {
  // Enviar pulso de trigger
  digitalWrite(PIN_TRIGGER, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_TRIGGER, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIGGER, LOW);
  
  // Medir tiempo de respuesta
  long duracion = pulseIn(PIN_ECHO, HIGH, 30000);
  
  // Calcular distancia (cm)
  // Velocidad sonido = 343 m/s = 0.0343 cm/μs
  // Distancia = tiempo * 0.0343 / 2
  long distancia = duracion * 0.0343 / 2;
  
  return distancia;
}

void loop() {
  long distancia = medirDistancia();
  
  Serial.print("Distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");
  
  // Representación visual
  int barras = distancia / 5;
  for (int i = 0; i < barras && i < 20; i++) {
    Serial.print("█");
  }
  Serial.println();
  
  delay(500);
}
