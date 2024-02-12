#include <DHT.h>
#include <WiFi.h>
#include <PubSubClient.h>

#define DHTPIN 4     // What digital pin the DHT11 is connected to (PIN 2 gives problems during the upload of the sketch, beware.)
#define DHTTYPE DHT11   // DHT 11
#define MAX_ATTEMPTS 20  // Maximum number of attempts to connect to wifi network

const char* ssid = "SSID";    // Your network's SSID
const char* password = "PASSWORD";   // Your network's password
const char* mqtt_server = "192.168.1.144";   // Raspberry Pi IP.
const int mqtt_port = 1883;
DHT dht(DHTPIN, DHTTYPE);
WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  dht.begin();
  connectToWifi();
}

void loop() {
  if (!client.connected()) {
    reconnect_mqtt();
  }
  client.loop();
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

  char temperatureString[8];
  dtostrf(temperature, 6, 2, temperatureString);
  client.publish("esp32/temperature", temperatureString);
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

void setup_mqtt() {
  client.setServer(mqtt_server, mqtt_port);
}

void reconnect_mqtt() {
  while (!client.connected()) {
    Serial.println("Attempting MQTT connection...");
    if (client.connect("ESP32Client")) {
      Serial.println("Connected to MQTT broker");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}