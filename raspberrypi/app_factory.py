from flask import Flask
from db_manager import db

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DB_USERNAME='pythonUser',
        DB_PASSWORD='pythonPWD',
        DB_URL='localhost',
        DB_NAME='weather',
    )

    app.db_manager = db(
        app.config['DB_USERNAME'],
        app.config['DB_PASSWORD'],
        app.config['DB_URL'],
        app.config['DB_NAME']
    )

    from views import views
    app.register_blueprint(views, url_prefix='/')

    return app