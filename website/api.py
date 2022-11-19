"""
  NOTE TO ALL TEAM MEMBERS: YOU ARE NOT SUPPOSED TO RUN THIS FILE DIRECTLY WITH
  PYTHON. PLEASE RUN `main.py` INSTEAD FROM THE PROJECT ROOT FOLDER.

  COMMAND TO RUN:
  `py main.py`
"""

from . import db
from .models import Listing

from flask import Blueprint, render_template, requests
from flask_restful import Api,Resource,reqparse,abort,fields,marshal_with



api = Blueprint('api', __name__)

user_listing_resource_fields = {   
  'uid': fields.Integer, #listing uid
  'owner_uid': fields.Integer, #user uid
  'requirements': fields.String,
  'price': fields.Float
}

listing_create_info = reqparse.RequestParser()
listing_create_info.add_argument('owner_uid', type = int, required = True)
listing_create_info.add_argument('requirements', type = str, help = 'Enter Cleaning Requirements', required = True)
listing_create_info.add_argument('price', type = float, help = 'Enter Price', required = True)

listing_update_info = reqparse.RequestParser()
listing_update_info.add_argument('requirements', type = str, help = 'Enter Cleaning Requirements')
listing_update_info.add_argument('price', type = float, help = 'Enter Price')



class UserListingCreate(Resource):
  @marshal_with(user_listing_resource_fields)
  def get(self, uid): 
    user_listing_info = Listing.query.filter_by(uid = uid).first()
    if not user_listing_info: 
      abort(404, message = "Could not find listing")
    return user_listing_info
  
  @marshal_with(user_listing_resource_fields)
  def post(self, uid):
    info = listing_create_info.parse_args() 
    new_listing = Listing(uid = uid, owner_uid = info['owner_uid'], requirements = info['requirements'], price = info['price'])
    db.session.add(new_listing)
    db.session.commit()
    return new_listing,201

  @marshal_with(user_listing_resource_fields)
  def delete(self,uid):
    user_listing_info = Listing.query.filter_by(uid = uid).first()
    db.session.delete(user_listing_info)
    db.commit()
  
  @marshal_with(user_listing_resource_fields)
  def patch(self,uid):
    info = listing_create_info.parse_args()
    user_listing_info = Listing.query.filter_by(uid=uid).first()
    if info['requirements']:
      user_listing_info.requirements = info['requirements']
    if info['price']:
      user_listing_info.price = info['price']
    
    db.session.add(user_listing_info)
    db.session.commit()