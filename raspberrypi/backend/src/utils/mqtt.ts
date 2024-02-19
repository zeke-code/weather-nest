import * as mqtt from 'mqtt';
import { format } from 'date-fns';
import { getConnection } from './database';
import { Message } from './interfaces';

const MQTT_BROKER_URL = 'mqtt://127.0.0.1';
const MQTT_DEFAULT_TOPIC = 'temperature';

class MQTTService {
    private client: mqtt.MqttClient;

    constructor() {
        this.client = mqtt.connect(MQTT_BROKER_URL, {
            port: 1883,
        });

        this.client.on('connect', () => {
            console.log('MQTT Client Connected');
            this.subscribe(MQTT_DEFAULT_TOPIC);
        });

        this.client.on('message', async (topic, message) => {
            await this.handleMessage(topic, message);
        });

        this.client.on('error', (error) => {
            console.error('MQTT Client Error:', error);
        });
    }

    public subscribe(topic: string = MQTT_DEFAULT_TOPIC) {
        this.client.subscribe(topic, {}, (error) => {
            if (error) {
                console.error(`Subscribe to topic ${topic} failed:`, error);
            } else {
                console.log(`Subscribed to topic "${topic}"`);
            }
        });
    }

    public async publish(topic: string, message: string | Buffer) {
        this.client.publish(topic, message, {}, (error) => {
            if (error) {
                console.error(`Publish to topic ${topic} failed:`, error);
            } else {
                console.log(`Message published to topic "${topic}"`);
            }
        });
    }

    private async handleMessage(topic: string, message: Buffer) {
        const msgPayload = message.toString();
        const msg: Message = JSON.parse(msgPayload);
        console.log(`Received message on topic "${topic}":`, msgPayload);

        const formattedDate = format(new Date(msg.timestamp * 1000), 'yyyy-MM-dd HH:mm:ss');

        try {
            const connection = await getConnection();
            await connection.execute(
                `INSERT INTO measurements (temperature, humidity, timestamp) VALUES (?, ?, ?)`,
                [msg.temperature, msg.humidity, formattedDate]
            );
            console.log('Successfully inserted entry into database.');
        } catch (error) {
            console.error('Error inserting message into database:', error);
        }
    }
}

// Exporting an instance to be reused across the application
export const mqttService = new MQTTService();
