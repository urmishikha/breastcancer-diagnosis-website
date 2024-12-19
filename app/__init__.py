# app/__init__.py
from flask import Flask
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    app.register_blueprint(bp)  # Register the blueprint
    return app

