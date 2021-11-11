from operator import pos
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
  
    app = Flask(__name__)

    app.config.from_object("config.app_config")

    db.init_app(app)

    



    return app