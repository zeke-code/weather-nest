import express, { Express } from 'express'
import bodyParser from 'body-parser'
import temperatureRouter from './routers/temperature-router'

const app: Express = express();
const port: number = 8000;

app.use(bodyParser.json());

app.use(temperatureRouter);

app.use(express.static('public'))
app.use(function(req, res, next) {
    res.setHeader('Content-Type', 'text/plain');
    res.status(404).send('Ops... page not found!');
})

app.listen(port, function() {
    console.log(`Listening on http://localhost:${port}`);
})