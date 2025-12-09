from flask import Flask
from app.config import config_by_name
from app.db import init_db
import os

def create_app():
    app = Flask("contact-book")
    env = os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_by_name[env])

    db_url = os.getenv("DATABASE_URL")
    if db_url:
        init_db(db_url)
        from app.db import engine, Base
        from app.models import Contact, Email, Phone
        Base.metadata.create_all(engine)
        
    from app.api import health_bp, contact_bp
    app.register_blueprint(health_bp)
    app.register_blueprint(contact_bp)

    return app
