/*
Sketch che sfrutta un multisensore per leggere pressione, luminosità
*/
#include <SPI.h>
#include <LoRa.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_TSL2561_U.h>
#include <Adafruit_BMP085_U.h>

float data1;
float data2;

//oggetto necessario per utilizzare il sensore di luminosità
Adafruit_TSL2561_Unified tsl = Adafruit_TSL2561_Unified(TSL2561_ADDR_FLOAT, 12345);

//oggetto necessario per utilizzare il sensore di pressione 
Adafruit_BMP085_Unified bmp = Adafruit_BMP085_Unified(10085);

void setup() {
  Serial.begin(9600);
  delay(1000);

  // switch off builtin led
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  Serial.println("LoRa Sender");
  //adafruit faether m0
  //LoRa.setPins(8, 4, 3); //set CS, reset, IRQ pin

  /*
  ##############################################
    Set up LoRa
  #############################################
  */ 
  
  //arduino mkr wan 1300
  LoRa.setPins(LORA_IRQ_DUMB, 6, 1); //set CS, reset, IRQ pin
  
  if (!LoRa.begin(868.1E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  tsl.enableAutoRange(true);  
  
  LoRa.setTxPower(10); //14 dbm, sono 25 milliwatt
  LoRa.setSpreadingFactor(7);
  LoRa.setSignalBandwidth(125E3);
  //LoRa.setSyncWord(0x34);

  /*
  ##############################################
  SetUp sensore luminosità
  ##############################################
  */
  if(!tsl.begin())
  {
    /* There was a problem detecting the TSL2561 ... check your connections */
    Serial.print("Ooops, no TSL2561 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  /* Changing the integration time gives you better sensor resolution (402ms = 16-bit data) */
   tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);      /* fast but low resolution */
   //tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_101MS);  /* medium resolution and speed   */
  // tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_402MS);  /* 16-bit data but slowest conversions */

  /*
  ##############################################
    Set Up sensore di pressione
  ##############################################
  */
  if(!bmp.begin())
  {
    /* There was a problem detecting the BMP085 ... check your connections */
    Serial.print("Ooops, no BMP085 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
}

int counter = 0;
void loop() {
  /* Un nuovo evento del sensore di luminosità!*/ 
  sensors_event_t event;
  tsl.getEvent(&event);
  /*un nuovo evento del sensore che rileva la pressione*/
  sensors_event_t event_p;
  bmp.getEvent(&event_p);
  
  Serial.print("Sending packet");
  data2 = event_p.pressure;
  data1 = event.light;
  Serial.println(data1);
  Serial.println(data2);
  // send packet
  
  counter++;
  for(long f=867300000; f<868000000; f+=200000){
    for(int sf=7; sf<11; sf++){
      LoRa.setFrequency(f);
      LoRa.setSpreadingFactor(sf);
      delay(200);
      Serial.println(f);
      Serial.println(sf);
      LoRa.beginPacket();
      LoRa.print(f);
      LoRa.print(" ");
      LoRa.print(sf);
      LoRa.print(" ");
      LoRa.print(counter);
      LoRa.endPacket();
      delay(4000);
    }
  }
 
 

  
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW);

  
  delay(10000);
}
