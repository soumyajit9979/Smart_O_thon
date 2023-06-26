#include <SPI.h>
#include <MFRC522.h>
#include <SoftwareSerial.h>
#define SS_PIN 10
#define RST_PIN 9

MFRC522 mfrc522(SS_PIN, RST_PIN);  	
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(50);
  Serial.end();
}

void loop() {
  // put your main code here, to run repeatedly:
  SPI.begin();      // Initiate SPI bus
  mfrc522.PCD_Init();
  delay(50);
  // Look for new cards
   
  if (!mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if (!mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  SPI.end();
 
  // Show UID on serial monitor
  Serial.begin(9600);
  delay(100);

  Serial.end();
  String content = "";
  
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
    Serial.begin(9600);
    delay(50);
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? "0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
    Serial.end();
    content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
    content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println();

  Serial.begin(9600);
  delay(50);
  

  Serial.end();
  content.toUpperCase();

  delay(2000);
  
//  if (content.substring(1) == "6D C0 8C 38") // change here the UID of the card/cards that you want to give access
//  {
//    Serial.begin(9600);
//    delay(50);
//    Serial.println("OK");
//    Serial.end();
//    
//  }
//  else 
//  {
//    Serial.begin(9600);
//    delay(50);
//    Serial.println("NOT OK");
//    Serial.end();
//    
//    
//  }

}