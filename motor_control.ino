#define MotorDirection 8
#define MotorSpeed 9
int SpeedVal = 0;
void setup() {
  pinMode(MotorDirection, OUTPUT);
  pinMode(MotorSpeed, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(Encoder_output_A),DC_Motor_Encoder,RISING);
}

void loop() {
  
  //Ramps up the speed in the clockwise direction.
  digitalWrite(MotorDirection, LOW);                  //Loop increases the speed slowly until it reaches max speed.
  for(SpeedVal = 0; SpeedVal < 255; SpeedVal++){
      analogWrite(MotorSpeed,SpeedVal);
      Serial.println(Count_pulses);       
      delay(40);
  }
for(SpeedVal = 255; SpeedVal >0; SpeedVal--){
      analogWrite(MotorSpeed,SpeedVal);
      Serial.println(Count_pulses); 
      delay(40);
  }  
}