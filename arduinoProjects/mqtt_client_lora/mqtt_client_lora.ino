#include <dht.h>
#include <SPI.h>
#include <LoRa.h>

#define DHT11_PIN A0
dht DHT;
void setup() {
  Serial.begin(9600);
  Serial.println(F("Start MQTT Example"));
  if (!LoRa.begin(868E6))
      Serial.println(F("init failed"));
  
  LoRa.setFrequency(868.0);
  LoRa.setTxPower(13);
  LoRa.setSyncWord(0x34);
  LoRa.setSpreadingFactor(7);
         
}

void loop() {
  LoRa.beginPacket();
  LoRa.print("<5678> ");
  LoRa.print("field1=");
  LoRa.print(DHT.read11(DHT11_PIN));
  LoRa.print("&field2=");
  LoRa.print(DHT.read11(DHT11_PIN));
  LoRa.endPacket();
  Serial.print("ok \n");
  delay(10000);
}
