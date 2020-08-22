#include <SPI.h>
#include <RH_RF95.h>

/*
//for feather m0 RFM9x
#define RFM95_CS 8
#define RFM95_RST 4
#define RFM95_INT 3
*/

// Change to 434.0 or other frequency, must match RX's freq! In Europe 868.0MHz
#define RF95_FREQ 868.1
 
// Singleton instance of the radio driver
//RH_RF95 rf95(RFM95_CS, RFM95_INT);
 
// Blinky on receipt
#define LED 13

uint8_t sf = 7;  //spreading factor
uint8_t cr4 = 8; //"denominatore" del tasso di codifica


void setup() {
  /*
  pinMode(LED, OUTPUT);     
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);
  */
  
  while (!Serial); // wait until serial console is open, remove if not tethered to computer
  Serial.begin(9600);
  delay(100);
  Serial.println("Feather LoRa RX Test!");
  
  // manual reset
  //digitalWrite(RFM95_RST, LOW);
  delay(10);
  //digitalWrite(RFM95_RST, HIGH);
  delay(10);
  
  while (!rf95.init()) {
    Serial.println("LoRa radio init failed");
    while (1);
  }


  
  Serial.println("LoRa radio init OK!");
 
  // Defaults after init are 434.0MHz, modulation GFSK_Rb250Fd250, +13dbM
  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }
  
  Serial.print("Set Freq to: "); Serial.println(RF95_FREQ);
 
  // Defaults after init are 868.0MHz, 13dBm, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on
 
  // The default transmitter power is 13dBm, using PA_BOOST.
  // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then 
  // you can set transmitter powers from 5 to 23 dBm:

  
  rf95.setTxPower(15, false);
  //modifiche opzionali
  rf95.setSpreadingFactor(sf); 
  //rf95.setCodingRate4(cr4);
  //rf95.setPayloadCRC(false);

}

int16_t packetnum = 0;

void loop() {
  delay(1000); // Wait 1 second between transmits, could also 'sleep' here!
  Serial.println("Transmitting..."); // Send a message to rf95_server
  
  
  char radiopacket[20] = "pacchetto #      ";
  
  itoa(packetnum++, radiopacket+9, 10);
  //itoa serve per convertire interi in stringhe
  
  Serial.print("Sending "); Serial.println(radiopacket);
  //radiopacket[19] = 0;
  
  Serial.println("Sending..."); delay(10);
  rf95.send((uint8_t *)radiopacket, 20);
  //digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("Waiting for packet to complete..."); delay(10);
  rf95.waitPacketSent();
  //digitalWrite(LED_BUILTIN, LOW);

}
