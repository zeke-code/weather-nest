# Weather Nest

Weather Nest è un progetto di Internet of Things (IoT) sviluppato per il corso di TSI, Unibo. Si basa sull'utilizzo di un Raspberry Pi come server web che adotta il MEVN stack tecnologico (MariaDB, Express.js, Vue.js, Node.js), un modulo ESP32 e un sensore DHT11. Il sensore DHT11 raccoglie dati ambientali quali temperatura e umidità, che l'ESP32 invia al Raspberry Pi tramite il protocollo MQTT. Questi dati vengono poi elaborati e visualizzati su una dashboard web, dove è possibile filtrare i risultati e aggiornare a distanza i parametri di configurazione dell'ESP32, sempre tramite MQTT.

## Tecnologie Usate

- **Raspberry Pi:** Agisce come server web centrale, ospitando la dashboard e elaborando i dati.
- **ESP32:** Microcontrollore che si connette al sensore DHT11 e invia i dati al Raspberry Pi.
- **Sensore DHT11:** Misura i dati ambientali, in particolare temperatura e umidità.
- **MEVN Stack:** Tech Stack utilizzato per lo sviluppo dell'applicazione web del progetto.
- **Nginx:** reverse proxy di Node.js.
- **Mosquitto:** MQTT broker.

## Setup
Il progetto Weather Nest si avvale di **Nginx** e di **Mosquitto**, MQTT broker. Avviare **Mosquitto**, e configurare **Nginx** come reverse proxy del server Node.

### 1. Hardware

Assicurarsi che il sensore DHT11 sia correttamente collegato al modulo ESP32, verificando i PIN di input e in output nel codice. L'ESP32 deve essere configurato per connettersi ad una rete e impostato per inviare i dati all'indirizzo IP del Raspberry Pi tramite MQTT.

### 2. Web Server

Questo progetto fa utilizzo di **Nginx**. Per funzionare correttamente necessita inoltre di un broker. Nel caso si stesse utilizzando Unix, è sufficiente installare **mosquitto** e avviare il servizio. Riguardo **Nginx**, è necessario configurarlo come reverse proxy

1. Aprire un terminale nel seguente path: **weather-nest/raspberrypi/frontend**.
2. Installare i pacchetti necessari eseguendo:
   ```
   npm i
   ```
3. Eseguire nel terminale il seguente comando:
```
npm run build
```
4. Rinominare la cartella in output **dist** in **dist-frontend**
5. Spostare la cartella al path **weather-nest/raspberrypi/backend**.
6. Aprire un terminale nel path **weather-nest/raspberrypi/backend**.
7. Installare i pacchetti necessari eseguendo:
```
npm i
```
8. Eseguire nel temrinale il seguente comando:
```
npm run build
```
9. Per avviare il web server a questo punto basterà digitare:
```
npm run start
```

## Crediti


- Ezechiele Spina - [zeke-code](https://github.com/zeke-code)

This project was created as an assignment for the Internet Of Things course of the Computer Systems Technologies department of the University of Bologna.