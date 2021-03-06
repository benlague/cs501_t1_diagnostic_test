# project/server/__init__.py

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from project.server.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)

from project.server import bcrypt, db
from project.server.models import User

@app.route('/users/index', methods = ['GET'])
def UsersIndex():
    q = db.session.query(User)
    all_users = []
    for row in q:
        all_users.append(row.email)
    all_users_string = ' '.join(map(str, all_users)) 
    return all_users_string