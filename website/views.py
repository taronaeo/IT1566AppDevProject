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

@views.route('/carlistings')
def carlistings():
  return render_template("car listings.html")
@views.route('/contractorlistings')
def contractorlistings():
  return render_template('contractor listings.html')
@views.route('/createcarlistings')
def createcarlistings():
  return render_template('create car listings.html')
@views.route('createcontractorlistings')
def createcontractorlistings():
  return render_template('create contractor listings.html')
@views.route('/updatecarlistings')
def updatecarlistings():
  return render_template('update car listings.html')
@views.route('/update contractor listings')
def updatecontractorlistings():
  return render_template('update contractor listings.html')
