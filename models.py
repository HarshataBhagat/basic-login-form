from flask_login import UserMixin
from . import db

class Sign_up(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    uname = db.Column(db.String(25), unique=True,nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)