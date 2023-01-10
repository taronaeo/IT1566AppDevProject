"""
  NOTE TO ALL TEAM MEMBERS: YOU ARE NOT SUPPOSED TO RUN THIS FILE DIRECTLY WITH
  PYTHON. PLEASE RUN `main.py` INSTEAD FROM THE PROJECT ROOT FOLDER.

  COMMAND TO RUN:
  `py main.py`
"""

import shelve
from . import DB_USER_LOCATION, DB_WALLET_LOCATION
from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
  return render_template('home.html')

@views.route('/wallet', methods=['GET', 'POST'])
@login_required
def wallet():
  with shelve.open(DB_WALLET_LOCATION) as db:
    wallet = db[current_user.email] # type: ignore

  return render_template("wallet.html", wallet=wallet)

@views.route('/retrieveacc')
@login_required
def retrieveacc():
  with shelve.open(DB_USER_LOCATION) as db:
    return render_template("retrieveacc.html", users=db)

@views.route('/signup')
def signup():
  return render_template("signup.html")

@views.route('/login')
def login():
  return render_template("login.html")

@views.route('/UpdateAcc')
def updateA():
  return render_template("UpdateAcc.html")

@views.route('/VehicleStore')
def VehicleStore():
  return render_template("VehicleStore.html")

@views.route('/UpdateVehicle')
def updateV():
  return render_template("UpdateVehicle.html")
