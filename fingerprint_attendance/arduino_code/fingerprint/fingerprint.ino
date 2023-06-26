// original

#include <Adafruit_Fingerprint.h>
#include <SoftwareSerial.h>


// SoftwareSerial bluetooth(10, 11); // RX pin 10, TX pin 11
SoftwareSerial mySerial(3, 2);
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

#define RELAY_PIN       13
#define ACCESS_DELAY    3000 // Keep lock unlocked for 3 seconds 


void setup()
{
  // set the data rate for the sensor serial port
  Serial.begin(9600);
//  bluetooth.begin(9600);
//  mySerial.begin(57600);
//  delay(5);
//  if (finger.verifyPassword()) 
//  {
//  } 
//  else 
//  {
//    while (1) { delay(1); }
//  }
  
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH);   //Switch off relay initially. Relay is LOW level triggered relay so we need to write HIGH.
}

void loop()
{
  mySerial.end();
//  delay(300);
//   bluetooth.begin(9600);
//   delay(300);
//   if (bluetooth.available()) { // check if there is incoming data
// //    Serial.println("GG");
//     char c = bluetooth.read(); // read a character
//     bluetooth.println(c); // print the character to the Serial Monitor
//     if(c=='1'){
//       digitalWrite(RELAY_PIN, LOW);
//       delay(ACCESS_DELAY);
//       digitalWrite(RELAY_PIN, HIGH);
//       Serial.println(55);
//       }
//     else if(c=='0'){
//       exit(0);
//     }

//       bluetooth.end();
//   }
// delay(50);
//   bluetooth.end();
  mySerial.begin(57600);
  delay(5);
  if (finger.verifyPassword()) 
  {
  } 
  else 
  {
    while (1) { delay(1); }
  }
  if ( getFingerPrint() != -1)
  {
  }

  // if(getFingerPrint()==4){
  //   Serial.println(4);
  //   exit(0);
  // }
  
  // bluetooth.end();
  mySerial.end();
  delay(50);            //Add some delay before next scan.

//  bluetooth.begin(9600);
}

// returns -1 if failed, otherwise returns ID #
int getFingerPrint() 
{
  int p = finger.getImage();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK)  return -1;
 
  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK)  return -1;

  Serial.println(finger.fingerID);
  
  
  // found a match!
  return finger.fingerID;
}