import paho.mqtt.client as mqtt
import time

def message (client, userdata, message):
    topic = str(message.topic)
    message = str(message.payload.decode('utf-8'))
    print(topic, ": ", message)
    
client = mqtt.Client('subscriber')
client.connect('localhost', 1883)
client.subscribe('testTopic')
client.on_message = message
client.loop_start()

while(1):
    time.sleep(0.5)