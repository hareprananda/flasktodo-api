from datetime import datetime
from enum import unique
from flask import Flask
from src.app.routes.api import app as api
import os
from flask import jsonify
from src.database import db
from flask_jwt_extended import JWTManager, jwt_required
from src.app.middleware.RegisterMiddleware import RegisterMiddleware


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
        app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']
        app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)

    JWTManager(app)
    RegisterMiddleware(app)

    app.register_blueprint(api, url_prefix='/api/v1')
    @app.errorhandler(404)
    def notFound(e):
        return jsonify({'message': 'Not found'}), 404

    return app

