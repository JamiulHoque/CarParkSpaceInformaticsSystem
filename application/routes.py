#!/usr/bin/python3

from application import app, db
from application.models import Carpark, Vehicle, AddVehicle, Delete, Update
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


