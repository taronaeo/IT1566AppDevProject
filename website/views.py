"""
  NOTE TO ALL TEAM MEMBERS: YOU ARE NOT SUPPOSED TO RUN THIS FILE DIRECTLY WITH
  PYTHON. PLEASE RUN `main.py` INSTEAD FROM THE PROJECT ROOT FOLDER.

  COMMAND TO RUN:
  `py main.py`
"""

from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
  return render_template('home.html')

@views.route('/wallet')
def wallet():
  return render_template("wallet.html")

@views.route('/retrieveacc')
@login_required
def retreieveacc():
  return render_template("retrieveacc.html")

@views.route('/signup')
def signup():
  return render_template("signup.html")

@views.route('/login')
def login():
  return render_template("login.html")
