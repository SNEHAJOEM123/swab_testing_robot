#include <ESP8266WiFi.h>
#include <ros.h>
#include <std_msgs/Int64.h>
#define ROSSERIAL_ARDUINO_TCP

#define ENCA D6
#define ENCB D5



ros::NodeHandle nh;


std_msgs::Int64 encoder;
ros::Publisher encoderValue("encoderValue", &encoder);

const char* ssid     = "AndroidAP9683";
const char* password = "usel8709";
// Set the rosserial socket server IP address
IPAddress server(192,168,43,214);
// Set the rosserial socket server port
const uint16_t serverPort = 11411;

int count=0;

ICACHE_RAM_ATTR void EncoderDataA() 
{
  if(digitalRead(ENCA) == LOW) 
  count--;
  else
  count++; 
}

void setup()
{
  // Use ESP8266 serial to monitor the process
  Serial.begin(115200);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  // Connect the ESP8266 the the wifi AP
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  // Set the connection to rosserial socket server
  nh.getHardware()->setConnection(server, serverPort);
  nh.initNode();

  // Another way to get IP
  Serial.print("IP = ");
  Serial.println(nh.getHardware()->getLocalIP());

  nh.advertise(encoderValue);
  pinMode(ENCA,INPUT_PULLUP);
  pinMode(ENCB,INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(ENCA), EncoderDataA, RISING);

}

void loop()
{

//  if (nh.connected()) {
//    Serial.println("Connected");
  encoder.data = count;
  encoderValue.publish( &encoder);
//  } else {
//    Serial.println("Not Connected");
//  }
  nh.spinOnce();
  // Loop exproximativly at 1Hz
  delay(1000);
}
