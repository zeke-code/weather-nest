from flask import Flask
import paho.mqtt.client as mqtt
from views import views
from db_manager import db_manager

app = Flask(__name__)

MQTT_BROKER_HOST = 'localhost'
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = 'temperature'

def on_connect(client, userdata, flags, rc):
    print('Connected to broker with state code: ' + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'subscriber')
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)
client.subscribe('temperature')
client.on_connect = on_connect
client.on_message = on_message
client.loop_start()

app.register_blueprint(views, url_prefix='/')
app.config['MYSQL_HOST'] = 'raspberrypi'
app.config['MYSQL_USER'] = 'pythonUser'
app.config['MYSQL_PASSWORD'] = 'pythonPWD'
app.config['MYSQL_DB'] = 'weather'

if __name__ == '__main__':
    app.run(port=8000, debug=True)