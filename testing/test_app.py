#!/usr/bin/python3

import unittest
from flask_testing import TestCase
from flask import url_for

from application import app, db
from application.models import Carpark, Vehicle

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///")
        app.config['SECRET_KEY'] = "testingtesting"
        return app
    def setUp(self):
        db.drop_all()
        db.create_all()

        testcarpark1=Carpark(name="testcarpark1", capacity="250")
        testcarpark2=Carpark(name="testcarpark2", capacity="400")
        testcarpark3=Carpark(name="testcarpark3", capacity="500")

        db.session.add(testcarpark1)
        db.session.add(testcarpark2)
        db.session.add(testcarpark3)

        db.session.commit()

        db.session.add_all([
            Vehicle(registration="BK06VRJ", make="Nissan", model="GTR", carpark=testcarpark1),
            Vehicle(registration="DG04TUU", make="Honda", model="Jazz", carpark=testcarpark2),
            Vehicle(registration="MK71VBH", make="Skoda", model="Superb", carpark=testcarpark3)])
        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestAccess(TestBase):
    def test_access_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    def test_access_Carpark(self):
        response=self.client.get(url_for('carpark', id=1))
        self.assertEqual(response.status_code, 200)

    def test_access_vehicle(self):
        response=self.client.get(url_for('vehicle', id=1))
        self.assertEqual(response.status_code, 200)

    def test_find_Carpark(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b'testcarpark1', response.data)

    def test_find_vehicle(self):
        response=self.client.get(url_for('carpark', id=1))
        self.assertIn(b'BK06VRJ', response.data)

class TestUpdate(TestBase):
    def test_update_vehicle(self):
        response = self.client.post(url_for('edit', carpark_id=1, id=1), data=dict(registration="hello"))
        self.assertIn(b'hello', response.data)

class TestDelete(TestBase):
    def test_delete_vehicle(self):
        response=self.client.get(url_for('delete', carpark_id=1, id=1), data=dict(registration="BK06VRJ"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestModels(TestBase):
    def test_Carpark_model(self):
        self.assertEqual(Carpark.query.count(), 3)

    def test_vehicle_model(self):
        self.assertEqual(Vehicle.query.count(), 3)
