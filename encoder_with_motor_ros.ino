#include <Arduino.h>
#include <ros.h>
#include <std_msgs/Int64.h>

ros::NodeHandle  nh;
#define ENCA D6
#define ENCB D5
#define ENCZ D7

#define PWM D2
#define DIR D1

int PWM_Value= 100;

std_msgs::Int64 encoder;
ros::Publisher encoderValue("encoderValue", &encoder);

volatile long count=0;

ICACHE_RAM_ATTR void EncoderDataA() 
{
  if(digitalRead(ENCB) == LOW) 
  count--;
  else
  count++; 
}

void setup()
{
  nh.initNode();
  nh.advertise(encoderValue);
  pinMode(ENCA,INPUT_PULLUP);
  pinMode(ENCB,INPUT_PULLUP);
  pinMode(PWM, OUTPUT);
  pinMode(DIR, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(ENCA), EncoderDataA, RISING);
}

void loop()
{
  encoder.data = count;
  encoderValue.publish( &encoder);
  if(count<8500)
  {
    digitalWrite(DIR,LOW);
    analogWrite(PWM,PWM_Value);
  }
  else
  {
    analogWrite(PWM,0);
  }
  nh.spinOnce();
  delay(1000);
}
