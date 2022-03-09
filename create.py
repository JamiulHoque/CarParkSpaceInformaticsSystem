#!usr/bin/python3

from application import app, db
from application.models import Carpark, Vehicle

db.drop_all()
db.create_all()

peelpark = Carpark(name = "Peel Park Campus", capacity = "250")
maxwell = Carpark(name = "Maxwell Building Carpark", capacity = "400")
frederick = Carpark(name = "Frederick Campus", capacity = "500")

db.session.add(peelpark)
db.session.add(maxwell)
db.session.add(frederick)
db.session.add_all([
    Vehicle(registration = "BL08JWM", make = "BMW", model = "1 Series", carpark = peelpark),
    Vehicle(registration = "ML71KHB", make = "Skoda", model = "Skala", carpark = frederick),
    Vehicle(registration = "BK06VRJ", make = "Nissan", model = "Note", carpark = maxwell)
])
db.session.commit()

