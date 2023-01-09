"""
  NOTE TO ALL TEAM MEMBERS: YOU ARE NOT SUPPOSED TO RUN THIS FILE DIRECTLY WITH
  PYTHON. PLEASE RUN `main.py` INSTEAD FROM THE PROJECT ROOT FOLDER.

  COMMAND TO RUN:
  `py main.py`
"""

from .models import User

from flask import Blueprint, render_template, request
from werkzeug.security import generate_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  # if request.method == 'POST':
  #   email = request.form.get('email')
  #   password = request.form.get('password')
  return render_template('login.html')

@auth.route('/logout')
def logout():
  return "<h1>Logout</h1>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template('signup.html')

  email = request.form.get('email')
  password = request.form.get('password')
  password_confirm = request.form.get('password_confirm')
  full_name = request.form.get('full_name')
  home_address = request.form.get('home_address')
  phone_number = request.form.get('phone_number')

  if not email or \
     not password or \
     not password_confirm or \
     not full_name or \
     not home_address or \
     not phone_number:
    return {"message": "Please ensure that all fields are filled out!"}

  if len(password) < 6 or len(password_confirm) < 6:
    return {"message": "Password must have a minimum length of 6 characters!"}

  if password != password_confirm:
    return {"message": "Passwords do not match!"}

  return {"message": "wait lol"}
