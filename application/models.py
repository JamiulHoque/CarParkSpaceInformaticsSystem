#!/usr/bin/python3

from application import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length


class Carpark(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    vehicles = db.relationship('Vehicle', backref='carpark')

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registration = db.Column(db.String(50), nullable=False)
    make = db.Column(db.String(15), nullable=False)
    model = db.Column(db.String(15), nullable=False)
    carpark_id = db.Column(db.Integer, db.ForeignKey('carpark.id'))


class AddVehicle(FlaskForm):
    registration = StringField('Registration', [Length(min=4, max=100)])
    make = StringField('Make', [Length(min=4, max=100)])
    model = StringField('Model', [Length(min=3, max=100)])
    submit = SubmitField('Add Vehicle')

class Delete(FlaskForm):
    submit = SubmitField("Delete Vehicle")

class Update(FlaskForm):
    submit = SubmitField("Update Vehicle")