#include <SPI.h>
#include <LoRa.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Receiver");

  // switch off builtin led
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  LoRa.setPins(8, 4, 3); //adafruit feather m0

  if (!LoRa.begin(868.1E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }

  LoRa.setSpreadingFactor(7);
}

void loop() {

  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    digitalWrite(LED_BUILTIN, HIGH);
    // received a packet
    Serial.print("Received packet '");

    // read packet
    while (LoRa.available()) {
      Serial.print((char)LoRa.read());
    }
    
    digitalWrite(LED_BUILTIN, LOW);

    // print RSSI of packet and SNR
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());
    Serial.print("' with SNR ");
    Serial.println(LoRa.packetSnr());
  }
}
