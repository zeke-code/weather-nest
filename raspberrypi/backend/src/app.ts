import express, { Express } from 'express'
import bodyParser from 'body-parser'
import history from 'connect-history-api-fallback'
import temperatureRouter from './routers/temperature-router'
import { mqttService } from './utils/mqtt';

const app: Express = express();
const port: number = 8000;

mqttService;

app.use(bodyParser.json());

app.use(temperatureRouter);

app.use(history)
app.use(express.static('public'));
app.use(express.static('dist-frontend'));
app.use(function(req, res, next) {
    res.setHeader('Content-Type', 'text/plain');
    res.status(404).send('Ops... page not found!');
})

app.listen(port, function() {
    console.log(`Listening on http://localhost:${port}`);
})