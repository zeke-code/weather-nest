import json
import paho.mqtt.client as mqtt
from datetime import datetime
from flask import current_app

MQTT_BROKER_HOST = 'localhost'
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = 'temperature'

def init_mqtt_client(app):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'subscriber')
    
    def on_connect(client, userdata, flags, rc):
        print('Connected to broker with state code: ' + str(rc))
        client.subscribe(MQTT_TOPIC)
        
    def on_message(client, userdata, message):
        msg_payload = message.payload.decode('utf-8')
        msg = json.loads(msg_payload)
        print(f'Received message: {msg}')
    
        timestamp = datetime.fromtimestamp(msg['timestamp'])
        formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
        elements = (msg['temperature'], msg['humidity'], formatted_timestamp)
        
        with app.app_context():
            db_manager = current_app.db_manager
            db_manager.insert(elements, 'measurements', 'temperature, humidity, timestamp')
    
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)
    client.loop_start()
