#include <ros.h>
#include <std_msgs/Int64.h>

ros::NodeHandle nh;

#define ENCA 2
#define ENCB 3

std_msgs::Int64 encoder;
ros::Publisher encoderValue("encoderValue",&encoder);

int count=0;

void EncoderDataA() 
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
  attachInterrupt(digitalPinToInterrupt(ENCA), EncoderDataA, RISING);
  
  
  
}

void loop()
{
  encoder.data=count;
  encoderValue.publish( &encoder);
  nh.spinOnce();
  delay(100);
}
