from faker import Faker
from faker_vehicle import VehicleProvider
from sqlalchemy.orm import sessionmaker

from models import db_engine, Driver, Vehicle
from utils import generate_plate_number

fkr = Faker()
fkr.add_provider(VehicleProvider)
session = sessionmaker(bind=db_engine)()


def create_drivers(drivers_amount=10):
    for _ in range(drivers_amount):
        first_name = fkr.first_name()
        last_name = fkr.last_name()
        driver = Driver(first_name=first_name, last_name=last_name)
        save_to_db(driver)


def create_vehicles(vehicles_amount=10):
    for _ in range(vehicles_amount):
        car = fkr.vehicle_make_model().split()
        make = car[0]
        model = ' '.join(car[1:])
        plate_number = generate_plate_number()
        vehicle = Vehicle(make=make, model=model, plate_number=plate_number)
        save_to_db(vehicle)


def save_to_db(obj):
    session.add(obj)
    session.commit()


def fill_db():
    create_drivers()
    create_vehicles()


fill_db()
