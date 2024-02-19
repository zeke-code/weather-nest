import * as mqtt from 'mqtt'
import { format } from 'date-fns'
import { Message } from './interfaces'

const MQTT_BROKER_HOST = 'mqtt://127.0.0.1';
const MQTT_BROKER_PORT = 1883;
const MQTT_DEFAULT_TOPIC = 'temperature';

export function initMqttClient() {
    const client = mqtt.connect(MQTT_BROKER_HOST, {
        clientId: 'subscriber',
        port: MQTT_BROKER_PORT
    });

    console.log('Trying to connect to a broker...')
    client.on('connect', () => {
        console.log('Connected to broker');
        client.subscribe(MQTT_DEFAULT_TOPIC, (err) => {
            if (!err) {
                console.log(`Subscribed to topic ${MQTT_DEFAULT_TOPIC}`);
            }
            else {
                console.log('Something went wrong trying to connect to broker. Check if host and port are correct.');
            }
        });
    });

    client.on('message', (topic, message) => {
        const msgPayload = message.toString();
        const msg: Message = JSON.parse(msgPayload);
        console.log('Received a message: ' + msgPayload);

    })

    client.on('error', function (error) {
        console.log('Something went wrong: ' + error);
    })
}
