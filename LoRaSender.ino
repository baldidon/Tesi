#include <SPI.h>
#include <LoRa.h>

int counter = 0;

void setup() {
  Serial.begin(9600);
  delay(1000);

  // switch off builtin led
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  Serial.println("LoRa Sender");

  LoRa.setPins(8, 4, 3); // set CS, reset, IRQ pin
  //rispetto a quelli impostati di default da questa libreria, questi sono quelli
  //necessari per lavorare con l'adafruit feather m0
  if (!LoRa.begin(868E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }

  LoRa.setSpreadingFactor(9);           // ranges from 6-12,default 7 see API docs
  Serial.println("LoRa init succeeded.");
}

void loop() {
  Serial.print("Sending packet: ");
  Serial.println(counter);
  
  
  // send packet
  LoRa.beginPacket();
  LoRa.print("hello ");
  LoRa.print(counter);
  LoRa.endPacket();
  delay(100);
 

  counter++;

  delay(5000);
}
