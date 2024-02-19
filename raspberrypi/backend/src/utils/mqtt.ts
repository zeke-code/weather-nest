import * as mqtt from 'mqtt'
import { format } from 'date-fns'
import { Message } from './interfaces'
import { getConnection } from './database';

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
        client.subscribe(MQTT_DEFAULT_TOPIC);
    });

    client.on('message', async (topic, message) => {
        const msgPayload = message.toString();
        const msg: Message = JSON.parse(msgPayload);
        console.log('Received a message: ' + msgPayload);
        const epoch = msg['timestamp'];
        const date = new Date(epoch * 1000);

        function pad(number: number) {
        return number < 10 ? '0' + number : number;
        }
        const formattedDate = date.getFullYear() + '-' + 
                                pad(date.getMonth() + 1) + '-' + 
                                pad(date.getDate()) + ' ' + 
                                pad(date.getHours()) + ':' + 
                                pad(date.getMinutes()) + ':' + 
                                pad(date.getSeconds());

        const connection = await getConnection();
        connection.execute(
            `INSERT INTO measurements (temperature, humidity, timestamp) VALUES (?, ?, ?)`,
            [msg.temperature, msg.humidity, formattedDate]
        );
        
    })

    client.on('error', function (error) {
        console.log('Something went wrong: ' + error);
    })
}