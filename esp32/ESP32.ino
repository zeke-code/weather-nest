#include <DHT.h>
#include <WiFi.h>
#include <PubSubClient.h>

#define DHTPIN 4     // What digital pin the DHT11 is connected to (PIN 2 gives problems during the upload of the sketch, beware.)
#define DHTTYPE DHT11   // DHT 11
#define MAX_ATTEMPTS 20  // Maximum number of attempts to connect to wifi network

const char* ssid = "Star Shopping";    // Your network's SSID
const char* password = "Samuezechia";   // Your network's password

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  connectToWifi();
}

void loop() {
  readTemperature();
}

void readTemperature() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // If value is not valid, exit early and retry.
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print("%  Temperature: ");
  Serial.print(temperature);
  Serial.println("°C ");
  delay(2000);
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