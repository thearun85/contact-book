from flask import Flask
from app.config import config_by_name
import os

def create_app():
    app = Flask("contact-book")
    env = os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_by_name[env])

    from app.api import health_bp
    app.register_blueprint(health_bp)

    return app
