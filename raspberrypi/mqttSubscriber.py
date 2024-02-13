import paho.mqtt.client as mqtt
import json
from db_manager import db_manager
import time

def on_message(client, userdata, message):
    msg_payload = message.payload.decode('utf-8')
    msg = json.loads(msg_payload)
    print(f'Received message: {msg}')

    elements = [(msg['temperature'], msg['humidity'], msg['timestamp'])]
    database.insert(elements, 'measurementsexit', 'temperature, humidity, timestamp')

database = db_manager('pythonUser', 'pythonPWD', 'localhost', 'weather')
    
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'subscriber')
client.connect('localhost', 1883)
client.subscribe('temperature')
client.on_message = on_message
client.loop_start()

while(1):
    time.sleep(0.5)