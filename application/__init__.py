#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:Password1!@database.cop4kgvc8v0g.eu-west-2.rds.amazonaws.com/carpark
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

from application import routes