from app_factory import create_app
from mqtt_client import init_mqtt_client

app = create_app()

if __name__ == '__main__':
    init_mqtt_client(app)
    app.run(port=8000, debug=True)
