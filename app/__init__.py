"""
Setup an initialization to delay the creation of the application after runtime.

This helps to enable the use of blueprint.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import config

db = SQLAlchemy()


def create_app(config_name):
    """Initialize the application after runtime."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    cors = CORS(app)

    # Register blueprint.
    from app.routes import api
    app.register_blueprint(api, url_prefix='/api')

    return app
