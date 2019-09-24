from flask import Flask
from flask_bootstrap import Bootstrap

from app.main import bp
from config import Config


bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(bp)
    bootstrap.init_app(app)
    return app

app = create_app()
