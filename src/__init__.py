from datetime import datetime
from enum import unique
from flask import Flask
from src.routes.api import app as api
import os
from src.database import db
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        dbUser = os.environ['MYSQL_USER']
        dbPassword = os.environ['MYSQL_PASSWORD']
        dbName = os.environ['MYSQL_DB']
        dbHost = os.environ['MYSQL_HOST']
        # add database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+dbUser+':'+dbPassword+'@'+dbHost+'/'+dbName
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)
    app.register_blueprint(api, url_prefix='/api/v1')

    return app

