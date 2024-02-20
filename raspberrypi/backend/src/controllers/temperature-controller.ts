import { Request, Response } from "express";
import { getConnection } from "../utils/database";
import { mqttService } from "../utils/mqtt";

export async function modifyConfiguration(req: Request, res: Response) {
    const message = { delay: req.body.delay, temperatureOffset: req.body.temperatureOffset,
        humidityOffset: req.body.humidityOffset
    }
    const messageString = JSON.stringify(message);
    mqttService.publish('esp32/config', messageString);
    res.status(200).send('Configuration updated successfully!');
}

export async function getTemperatures(req: Request, res: Response) {
    const connection = await getConnection();
    const [measurements] = await connection.execute(
        `SELECT * FROM measurements`,
        []
    );
    res.json(measurements);
}