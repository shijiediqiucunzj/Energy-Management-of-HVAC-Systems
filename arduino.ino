/* FYP2017
 * Arduino code to send room conditions to pi via zigbee
 * Command HVAC elements based on commands sent from pi via zigbee
 * Author: Kunal Jagadeesh
 * License: Public Domain
 */

#include <SoftwareSerial.h>
#include "DHT.h"

/* Connections
 * Connect DHT22 data pin to pin 2 
 * Connect cooler vcc to pin 5
 * Connect heater vcc to pin 7
 * Connect humidifier vcc to pin 9
 * Connect exhaust vcc to pin 11
 * Make common ground
 */
#define DHTPIN 2 
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

int cooler = 5; 
int heater = 7; 
int humidifier = 9; 
int exhaust = 11;  
int ELED = 13;
SoftwareSerial Xbee(0,1);

void setup()
{
  pinMode(cooler, OUTPUT);
  pinMode(heater, OUTPUT);
  pinMode(humidifier, OUTPUT);
  pinMode(exhaust, OUTPUT);
  pinMode(ELED, OUTPUT);
  dht.begin();
  Serial.begin(9600);
  Xbee.begin(9600);
}

void loop() 
{
  if(Xbee.available())
  {
    char ch = Xbee.read();
    switch(ch)
    {
      case 's':
        sendSensorData();
        break;
      case 'c':
        run_cooler();
        break;
      case 'f':
        run_heater();
        break;
      case 'h':
        run_humidifier();
        break;
      case 'e':
        run_exhaust();
        break;
      case 'x':
	raise_error();
	break;
    }
  }
}

void sendSensorData()
{
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  Serial.print(h);
  Serial.println(t);
}

void run_cooler()
{
  if (digitalRead(heater) == HIGH)
  {
    digitalWrite(heater, LOW);
    delay(500);
  }
  digitalWrite(cooler, HIGH);
  delay(500);
}

void run_heater()
{
  digitalWrite(cooler, HIGH);
  delay(500);
  digitalWrite(heater, HIGH); /*both heater and fan should run for this case*/
  delay(500);
}

void run_humidifier()
{
  if(digitalRead(exhaust) == HIGH)
  {
    digitalWrite(exhaust, LOW);
    delay(500);
  }
  digitalWrite(humidifier, HIGH);
  delay(500);
}

void run_exhaust()
{
  if(digitalRead(humidifier) == HIGH)
  {
    digitalWrite(humidifier, LOW);
    delay(500);
  }
  digitalWrite(exhaust, HIGH);
  delay(500);
}

void raise_error()
{
  int n = 3;
  while(n--)
  {
    digitalWrite(ELED, HIGH);
    delay(1000);
    digitalWrite(ELED, LOW);
    delay(1000);
}