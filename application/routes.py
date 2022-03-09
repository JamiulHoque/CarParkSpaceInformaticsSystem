#!/usr/bin/python3

from application import app, db
from application.models import Carpark, Vehicle, AddVehicle, Delete, Update
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method =="GET":
       return render_template("index.html", query=Carpark.query.all())



@app.route('/carpark/<id>', methods = ["GET", "POST"])
def carpark(id):
    if request.method == "GET":
        return render_template("update.html", carpark= Carpark.query.filter_by(id=id).first(), query=Vehicle.query.filter_by(carpark_id=id))

@app.route('/vehicle/<id>', methods = ["GET", "POST"])
def vehicle(id):
    form=AddVehicle()
    if request.method == "POST":
        new_vehicle=Vehicle(registration=form.registration.data, make=form.make.data, model=form.model.data, carpark_id=id)
        if not form.validate_on_submit():
            return render_template('vehicleerror.html', form=form)
        else:
            db.session.add(new_vehicle)
            db.session.commit()
            return redirect(url_for("carpark", id=new_vehicle.carpark_id))
    return render_template('vehicle.html', form=form)

@app.route('/delete/<carpark_id>/<id>')
def delete(carpark_id, id):
    car = Vehicle.query.filter_by(id=id).first()
    i = car.id
    shay = Vehicle.query.filter_by(carpark_id=carpark_id).first()
    j = shay.carpark_id
    if car is not None:
        db.session.delete(car)
        db.session.commit()
        return redirect(url_for("carpark", id=j))



@app.route('/edit/<carpark_id>/<id>', methods = ["GET", "POST"])
def edit(carpark_id, id):
    form=AddVehicle()
    vehicleedit = Vehicle.query.filter_by(id=id).first()
    if request.method =="POST":
        vehicleedit.registration=form.registration.data
        vehicleedit.make=form.make.data
        vehicleedit.model=form.model.data
        if not form.validate_on_submit():
            return render_template('editerror.html', form=form, vehicleedit=vehicleedit)
        else:
            db.session.commit()
            return redirect(url_for("carpark", id=vehicleedit.carpark_id))
    return render_template("edit.html", form=form, vehicleedit=vehicleedit)