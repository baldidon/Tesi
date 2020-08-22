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
  //adafruit faether m0
  //LoRa.setPins(8, 4, 3); //set CS, reset, IRQ pin

  //arduino mke wan 1300
  LoRa.setPins(LORA_IRQ_DUMB, 6, 1); //set CS, reset, IRQ pin

  
  if (!LoRa.begin(868.1E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  
    LoRa.setTxPower(14);
    LoRa.setSpreadingFactor(7);
    //setCodingRate
    //setPreambleLength
}

void loop() {
  Serial.print("Sending packet: ");
  Serial.println(counter);

  // send packet
  LoRa.beginPacket();
  LoRa.print("hello ");
  LoRa.print(counter);
  LoRa.endPacket();
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW);

  counter++;

  delay(5000);
}
