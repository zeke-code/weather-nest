import paho.mqtt.client as mqtt
import time

client = mqtt.Client('publisher')
client.connect()
client.loop_start()

while(1):
    client.publish('testTopic', 'testMessage')
    time.sleep(2)
    