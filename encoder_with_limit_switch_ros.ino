#include <Arduino.h>
#include <ros.h>
#include <std_msgs/Int64.h>

ros::NodeHandle  nh;
#define ENCA D6
#define ENCB D5
#define LS1 D4

std_msgs::Int64 encoder;
ros::Publisher encoderValue("encoderValue", &encoder);

int count=0;

ICACHE_RAM_ATTR void EncoderDataA() 
{
  if(digitalRead(ENCB) == LOW) 
  count--;
  else
  count++; 
}

ICACHE_RAM_ATTR void LimitSwitch()
{
  count=0;
}

void setup()
{
  //nh.getHardware()->setBaud(57600);
  nh.initNode();
  nh.advertise(encoderValue);
  pinMode(ENCA,INPUT_PULLUP);
  pinMode(ENCB,INPUT_PULLUP);
  pinMode(LS1, INPUT);
  attachInterrupt(digitalPinToInterrupt(ENCA), EncoderDataA, RISING);
  attachInterrupt(digitalPinToInterrupt(LS1), LimitSwitch, FALLING);
}

void loop()
{
  encoder.data = count;
  encoderValue.publish( &encoder);
  nh.spinOnce();
  delay(1000);
}
