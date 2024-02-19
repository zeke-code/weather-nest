import { Request, Response } from "express";
import { getConnection } from "../utils/database";
import { mqttService } from "../utils/mqtt";

export async function modifyConfiguration(req: Request, res: Response) {
    const message = { delay: req.body.delay, temperatureOffset: req.body.temperatureOffset,
        humidityOffset: req.body.humidityOffset
    }
    mqttService.publish('esp32/config', 'Hello World!');
    res.status(200).send('Configuration updated successfully!');
}