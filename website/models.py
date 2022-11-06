"""
  NOTE TO ALL TEAM MEMBERS: YOU ARE NOT SUPPOSED TO RUN THIS FILE DIRECTLY WITH
  PYTHON. PLEASE RUN `main.py` INSTEAD FROM THE PROJECT ROOT FOLDER.

  COMMAND TO RUN:
  `py main.py`
"""

from sqlalchemy.sql import func

from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):  # type: ignore
  uid = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), nullable=False, unique=True)
  password = db.Column(db.String(64), nullable=False)
  full_name = db.Column(db.String(150), nullable=False)
  home_address = db.Column(db.String(150), nullable=False)
  phone_number = db.Column(db.String(150), nullable=False)
  vehicles = db.relationship('Vehicle')

class Vehicle(db.Model):  # type: ignore
  # Vehicle License Plate
  uid = db.Column(db.String(150), primary_key=True)
  owner_uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
  vehicle_make = db.Column(db.String(150), nullable=False)
  vehicle_model = db.Column(db.String(150), nullable=False)
  unlock_system_installed = db.Column(db.Boolean, default=False)
  created_at = db.Column(db.DateTime(timezone=True), default=func.now())

class Wallet(db.Model):  # type: ignore
  uid = db.Column(db.Integer, db.ForeignKey('user.uid'), primary_key=True)
  balance = db.Column(db.Float, nullable=False)
  stamps_collected = db.Column(db.Integer, nullable=False, default=0)
  transactions = db.relationship('WalletTransaction')

class WalletTransaction(db.Model):  # type: ignore
  uid = db.Column(db.Integer, primary_key=True)
  wallet_uid = db.Column(db.Integer, db.ForeignKey('wallet.uid'))
  transaction_type = db.Column(db.String(150), nullable=False)
  transaction_amount = db.Column(db.Float, nullable=False)
  transaction_remarks = db.Column(db.String(150), nullable=False)
  transaction_timestamp = db.Column(db.DateTime(timezone=True), default=func.now())

class Listing(db.Model):  # type: ignore
  uid = db.Column(db.Integer, primary_key=True)
  owner_uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
  requirements = db.Column(db.String(150), nullable=False)
  price = db.Column(db.Float, nullable=False)
  transactions = db.relationship('ListingTransaction')

class ListingTransaction(db.Model):  # type: ignore
  uid = db.Column(db.Integer, db.ForeignKey('listing.uid'), primary_key=True)
  start_photos = db.Column(db.String(150), nullable=False)
  start_damages = db.Column(db.String(150), nullable=True)
  start_timestamp = db.Column(db.DateTime(timezone=True), default=func.now())
  end_photos = db.Column(db.String(150), nullable=False)
  end_timestamp = db.Column(db.DateTime(timezone=True))
  final_price = db.Column(db.Float, nullable=False)
