/*
  Sensor de Temperatura DHT22 - Arduino
  =====================================
  Hardware: Arduino UNO/Nano
  Componentes: Sensor DHT22 (temperatura y humedad)
  Conexionado: Pin 2 -> DATA
  Librería: DHT sensor library (Adafruit)
*/

#include <DHT.h>

const int PIN_DHT = 2;
const int TIPO_DHT = DHT22;

DHT dht(PIN_DHT, TIPO_DHT);

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("Sensor DHT22 iniciado");
}

void loop() {
  // Leer humedad
  float humedad = dht.readHumidity();
  // Leer temperatura (Celsius)
  float temperatura = dht.readTemperature();
  
  // Verificar lectura válida
  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error: Lectura del sensor falló");
    delay(2000);
    return;
  }
  
  // Mostrar resultados
  Serial.print("Humedad: ");
  Serial.print(humedad);
  Serial.println(" %");
  
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" °C");
  
  // Índice de calor
  float calor = dht.computeHeatIndex(temperatura, humedad, false);
  Serial.print("Índice de calor: ");
  Serial.print(calor);
  Serial.println(" °C");
  
  Serial.println("---");
  delay(2000);
}
