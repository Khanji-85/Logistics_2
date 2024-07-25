import os
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import flask_login

#create instance
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = flask_login.LoginManager()


def create_app():
    app = Flask(__name__)
    app.config['FLASK_APP'] = "main"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost:5432/testtest'
    app.config["SECRET_KEY"] = '1ccc03141ef776dc9afaf0776079cf90e3b5f3d3f259680a2b703feb99af9128'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SESSION_TYPE'] = "filesystem"
    app.config['PERMANENT_SESSION_LIFETIME'] = 33330  # 30 minutes in seconds

    #init
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # CORS(app)  # Enable CORS for all routes
    # Session(app)

    with app.app_context():
        print("yes")
        db.create_all()  # Create database tables for our data models
    return app
#
