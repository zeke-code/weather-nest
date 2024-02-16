from flask import Flask
import json
import paho.mqtt.client as mqtt
from views import views
from db_manager import db
from datetime import datetime

app = Flask(__name__)

MQTT_BROKER_HOST = 'localhost'
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = 'temperature'

def on_connect(client, userdata, flags, rc):
    print('Connected to broker with state code: ' + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, message):
    msg_payload = message.payload.decode('utf-8')
    msg = json.loads(msg_payload)
    print(f'Received message: {msg}')

    timestamp = datetime.fromtimestamp(msg['timestamp'])
    formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    elements = ((msg['temperature'], msg['humidity'], formatted_timestamp))
    db_manager = db(
        app.config['DB_USERNAME'],
        app.config['DB_PASSWORD'],
        app.config['DB_URL'],
        app.config['DB_NAME'])
    db_manager.insert(elements, 'measurements', 'temperature, humidity, timestamp')

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'subscriber')
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)
client.subscribe('temperature')
client.on_connect = on_connect
client.on_message = on_message
client.loop_start()
app.config['DB_USERNAME'] = 'pythonUser'
app.config['DB_PASSWORD'] = 'pythonPWD'
app.config['DB_URL'] = 'localhost'
app.config['DB_NAME'] = 'weather'



app.register_blueprint(views, url_prefix='/')


if __name__ == '__main__':
    app.run(port=8000, debug=True)

