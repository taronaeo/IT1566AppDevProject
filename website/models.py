"""
  ! NOTE TO ALL TEAM MEMBERS: YOU ARE NOT SUPPOSED TO RUN THIS FILE DIRECTLY WITH
  ! PYTHON. PLEASE RUN `main.py` INSTEAD FROM THE PROJECT ROOT FOLDER.

  ! COMMAND TO RUN:
  ! `py main.py`
"""

import shelve, random, string

from . import DB_BASE_LOCATION
from flask_login import UserMixin

class User(UserMixin):
  def __init__(
    self,
    email,
    password,
    full_name,
    home_address,
    phone_number,
    uid = None,
    vehicles = None,
    bank_information = None,
    training_complete = False,
    background_check = False
  ) -> None:
    super().__init__()
    self.uid = uid
    self.email = email
    self.password = password
    self.full_name = full_name
    self.home_address = home_address
    self.phone_number = phone_number
    self.vehicles = vehicles
    self.bank_information = bank_information
    self.training_complete = training_complete
    self.background_check = background_check
  
  @staticmethod
  def create_user(
    email,
    password,
    full_name,
    home_address,
    phone_number
  ):
    return User(
      email,
      password,
      full_name,
      home_address,
      phone_number,
      uid=email,
      vehicles=[],
      bank_information="",
      training_complete=False,
      background_check=False
    )
  
  def get_id(self):
    return (self.email)

class Vehicle():
  def __init__(self, uid, owner_uid, vehicle_make, vehicle_model, unlock_system_installed, created_at) -> None:
    self.uid = uid  # Vehicle License Plate
    self.owner_uid = owner_uid
    self.vehicle_make = vehicle_make
    self.vehicle_model = vehicle_model
    self.unlock_system_installed = unlock_system_installed
    self.created_at = created_at

class Wallet():
  def __init__(self, uid, balance, stamps_collected, transactions) -> None:
    self.uid = uid
    self.balance = balance
    self.stamps_collected = stamps_collected
    self.transactions = transactions
  
  @staticmethod
  def create_wallet(email):
    return Wallet(email, 0, 0, [])

class WalletTransaction():
  def __init__(self, transaction_type, transaction_amount, transaction_remarks, transaction_timestamp) -> None:
    self.transaction_type = transaction_type
    self.transaction_amount = transaction_amount
    self.transaction_remarks = transaction_remarks
    self.transaction_timestamp = transaction_timestamp

class Listing():
  def __init__(self, uid, owner_uid, requirements, price, transactions) -> None:
    self.uid = uid
    self.owner_uid = owner_uid
    self.requirements = requirements
    self.price = price
    self.transactions = transactions
  
  @staticmethod
  def get(uid):
    with shelve.open(DB_BASE_LOCATION) as db:
      try:
        return db['Listing'][uid]
      except KeyError:
        return None

class ListingTransaction():
  def __init__(self, uid, start_photos, start_damages, start_timestamp, end_photos, end_timestamp, final_price) -> None:
    self.uid = uid
    self.start_photos = start_photos
    self.start_damages = start_damages
    self.start_timestamp = start_timestamp
    self.end_photos = end_photos
    self.end_timestamp = end_timestamp
    self.final_price = final_price
  
  @staticmethod
  def get(uid):
    with shelve.open(DB_BASE_LOCATION) as db:
      try:
        return db['ListingTransaction'][uid]
      except KeyError:
        return None
