#include <DHT.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include <WiFiUdp.h>
#include <NTPClient.h>

#define DHTPIN 4     // What digital pin the DHT11 is connected to (PIN 2 gives problems during the upload of the sketch, beware.)
#define DHTTYPE DHT11   // DHT 11
#define MAX_ATTEMPTS 20  // Maximum number of attempts to connect to wifi network

const char* ssid = "Star Shopping";    // Your network's SSID
const char* password = "Samuezechia";   // Your network's password
const char* mqtt_server = "192.168.1.144";   // Raspberry Pi IP.
const int mqtt_port = 1883;
const char* mqtt_topic="temperature";   // MQTT Topic.
const char* mqtt_callback="esp32/config";
const char* ntpServer = "pool.ntp.org";   // NTP server for clock
const long utcOffset = 3600;    // Your country's time zone offset
float temperature_offset = 0;
float humidity_offset = 0;

int measure_delay = 10000;    // Measurements delay

DHT dht(DHTPIN, DHTTYPE);
WiFiClient espClient;
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, ntpServer, utcOffset);
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  dht.begin();
  connectToWifi();
  timeClient.begin();
  delay(1000);
  client.setServer(mqtt_server, mqtt_port);
  client.subscribe(mqtt_callback);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect_mqtt();
  }
  client.loop();
  timeClient.update();
  readTemperature();
  delay(measure_delay);
}

void readTemperature() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // If value is not valid, exit early and retry.
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  humidity += humidity_offset;
  temperature += temperature_offset;
  humidity = round(humidity * 100) / 100.0;
  temperature = round(temperature * 100) / 100.0;

  Serial.printf("Humidity: %.2f%%  Temperature: %.2f°C  Time: %ld \n", humidity, temperature, timeClient.getEpochTime());

  StaticJsonDocument<200> doc;
  doc["temperature"] = temperature;
  doc["humidity"] = humidity;
  doc["timestamp"] = timeClient.getEpochTime();

  char jsonOutput[128];
  serializeJson(doc, jsonOutput);
  client.publish(mqtt_topic, jsonOutput);
}

void connectToWifi() {
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < MAX_ATTEMPTS) {
    delay(1000);
    Serial.print("Failed to connect... retrying attempt ");
    Serial.println(attempts);
    attempts++;
  }
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nConnected to the WiFi network");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("\nFailed to connect to WiFi. Check SSID or password. Restarting...");
    ESP.restart();
  }
}

void reconnect_mqtt() {
  while (!client.connected()) {
    Serial.println("Attempting MQTT connection...");
    if (client.connect("ESP32Client", "admin", "admin")) {
      Serial.println("Connected to MQTT broker");
      client.subscribe(mqtt_callback);
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.println("Entering callback function.");
  String message;
  for (unsigned int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  StaticJsonDocument<256> doc;
  DeserializationError error = deserializeJson(doc, message);

  if (error) {
    Serial.print(F("deserializeJson() failed: "));
    Serial.println(error.f_str());
    return;
  }

  int delayPayload = doc["delay"];
  float temperatureOffsetPayload = doc["temperatureOffset"];
  float humidityOffsetPayload = doc["humidityOffset"];

  Serial.print("New delay: ");
  Serial.println(delayPayload);
  Serial.print("New Temperature Offset: ");
  Serial.println(temperatureOffsetPayload);
  Serial.print("New Humidity Offset: ");
  Serial.println(humidityOffsetPayload);

  measure_delay = delayPayload;
  temperature_offset = temperatureOffsetPayload;
  humidity_offset = humidityOffsetPayload;
}
