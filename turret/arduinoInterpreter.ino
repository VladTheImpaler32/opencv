#include<Servo.h>

Servo serX;
Servo serY;

String serialData;

void setup() {

  serX.attach(0,450,2200);
  serY.attach(2,950,2200);
  Serial.begin(115200);
  Serial.setTimeout(10);
}

void loop() {
  //lol
}

void serialEvent() {
  serialData = Serial.readString();
  serX.write(parseDataX(serialData));
  serY.write(parseDataY(serialData));
}

int parseDataX(String data){
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);
  return data.toInt();
}

int parseDataY(String data){
  data.remove(0,data.indexOf("Y") + 1);
  return data.toInt();
}
