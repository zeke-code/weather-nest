import { Request, Response } from "express";
import { getConnection } from "../utils/database";

export async function modifyConfiguration(req: Request, res: Response) {
    res.status(200).send('Yo mama');
}