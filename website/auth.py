"""
  NOTE TO ALL TEAM MEMBERS: YOU ARE NOT SUPPOSED TO RUN THIS FILE DIRECTLY WITH
  PYTHON. PLEASE RUN `main.py` INSTEAD FROM THE PROJECT ROOT FOLDER.

  COMMAND TO RUN:
  `py main.py`
"""

from . import DB_USER_LOCATION, DB_WALLET_LOCATION
from .models import User, Wallet

import shelve
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    if email == None or password == None:
      return redirect(url_for('auth.login'))

    with shelve.open(DB_USER_LOCATION) as db:
      if email not in db:
        return redirect(url_for('auth.login'))

      user = db[email]
      if user.password == password:
        login_user(user, remember=True)
        return redirect(url_for('views.retrieveacc'))

  return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
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
      return redirect(url_for('auth.signup'))

    if password != password_confirm:
      return redirect(url_for('auth.signup'))

    with shelve.open(DB_USER_LOCATION) as db_user, \
         shelve.open(DB_WALLET_LOCATION) as db_wallet:
      if email in db_user:
        return redirect(url_for('auth.signup'))

      user = User.create_user(email, password, full_name, home_address, phone_number)
      wallet = Wallet.create_wallet(email)
      db_user[email] = user
      db_wallet[email] = wallet

    login_user(user, remember=True)
    return redirect(url_for('views.retrieveacc'))

  return render_template('signup.html')
