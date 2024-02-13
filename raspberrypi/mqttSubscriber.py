import paho.mqtt.client as mqtt
import json
from db_manager import db_manager
import time
from datetime import datetime

def on_message(client, userdata, message):
    msg_payload = message.payload.decode('utf-8')
    msg = json.loads(msg_payload)
    print(f'Received message: {msg}')

    timestamp = datetime.fromtimestamp(msg['timestamp'])
    formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    elements = [(msg['temperature'], msg['humidity'], formatted_timestamp)]
    database.insert(elements, 'measurements', 'temperature, humidity, timestamp')

database = db_manager('pythonUser', 'pythonPWD', 'localhost', 'weather')
    
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'subscriber')
client.connect('localhost', 1883)
client.subscribe('temperature')
client.on_message = on_message
client.loop_start()

while(1):
    time.sleep(0.5)