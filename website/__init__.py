"""
  NOTE TO ALL TEAM MEMBERS: YOU ARE NOT SUPPOSED TO RUN THIS FILE DIRECTLY WITH
  PYTHON. PLEASE RUN `main.py` INSTEAD FROM THE PROJECT ROOT FOLDER.

  COMMAND TO RUN:
  `py main.py`
"""

from os import path
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'sgdetailmart.sqlite'

def create_app():
  app = Flask(__name__)
  api = Api(app)

  app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz' # NOTE: To be changed when deploying
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

  db.init_app(app)

  from .auth import auth
  from .views import views
  from .api import ListingApi

  app.register_blueprint(auth, url_prefix='/')
  app.register_blueprint(views, url_prefix='/')
  api.add_resource(ListingApi, "/api/listing", "/api/listing/<string:uid>") # Python types are not recognised for Flask_Restful package. Ignore redline.

  from .models import User, Vehicle, Wallet

  create_database(app)

  return app

def create_database(app):
  if not path.exists('website/' + DB_NAME):
    with app.app_context():
      db.create_all()
      print('Created Database!')
