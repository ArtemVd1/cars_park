from flask import Flask, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from models import Driver, Vehicle
from utils import (
    get_one_driver,
    get_one_vehicle,
    get_all_vehicle,
    get_vehicle_with_driver,
    get_vehicle_without_driver,
    get_all_drivers,
    get_drivers_create_after_date,
    get_drivers_create_before_date,
    replace_symbol_in_string
)
from validator import (
    driver_parser,
    vehicle_parser,
    driver_id_parser
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///cars_park.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)


class DriversList(Resource):
    def get(self):
        if request.args.get('created_at__gte'):
            tmp_gte = str(request.args.get('created_at__gte'))
            created_at__gte = replace_symbol_in_string(tmp_gte)
            return get_drivers_create_after_date(created_at__gte)
        elif request.args.get('created_at__lte'):
            tmp_lte = str(request.args.get('created_at__lte'))
            created_at__lte = replace_symbol_in_string(tmp_lte)
            return get_drivers_create_before_date(created_at__lte)
        else:
            return get_all_drivers()

    def post(self):
        if request.is_json:
            data = driver_parser.parse_args()
            new_driver = Driver(first_name=data['first_name'],
                                last_name=data['last_name'])
            db.session.add(new_driver)
            db.session.commit()
            return {'message': f'Driver {new_driver.first_name} {new_driver.last_name} has been created successfully'}
        else:
            return {'error': 'The request payload is not in JSON format'}


class DriverInfo(Resource):
    def get(self, driver_id):
        return get_one_driver(driver_id)

    def put(self, driver_id):
        if request.is_json:
            data = driver_parser.parse_args()
            db.session.query(Driver).filter(Driver.id == driver_id).update(
                {'first_name': data['first_name'],
                 'last_name': data['last_name']}, synchronize_session='fetch')
            db.session.commit()
            return {'message': f'Driver {data["first_name"]} {data["last_name"]} successfully updated'}
        else:
            return {'error': 'The request payload is not in JSON format'}

    def delete(self, driver_id):
        driver_first_name = get_one_driver(driver_id)[0]['first_name']
        driver_last_name = get_one_driver(driver_id)[0]['last_name']
        db.session.query(Driver).filter(Driver.id == driver_id).delete()
        db.session.commit()
        return {'message': f'Driver {driver_first_name} {driver_last_name} successfully deleted'}


class VehiclesList(Resource):
    def get(self):
        if str(request.args.get('with_drivers')) == 'yes':
            return get_vehicle_with_driver()
        elif str(request.args.get('with_drivers')) == 'no':
            return get_vehicle_without_driver()
        else:
            return get_all_vehicle()

    def post(self):
        if request.is_json:
            data = vehicle_parser.parse_args()
            new_vehicle = Vehicle(driver_id=data['driver_id'],
                                  make=data['make'],
                                  model=data['model'],
                                  plate_number=data['plate_number'])
            db.session.add(new_vehicle)
            db.session.commit()
            return {'message': f'Vehicle {new_vehicle.make} {new_vehicle.model} - {new_vehicle.plate_number} '
                               f'has been created successfully'}
        else:
            return {'error': 'The request payload is not in JSON format'}


class VehicleInfo(Resource):
    def get(self, vehicle_id):
        return get_one_vehicle(vehicle_id)

    def put(self, vehicle_id):
        if request.is_json:
            data = vehicle_parser.parse_args()
            db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).update(
                {'driver_id': data['driver_id'],
                 'make': data['make'],
                 'model': data['model'],
                 'plate_number': data['plate_number'],
                 }, synchronize_session='fetch')
            db.session.commit()
            return {'message': f"Vehicle {data['make']} {data['model']} - {data['plate_number']} successfully updated"}
        else:
            return {'error': 'The request payload is not in JSON format'}

    def delete(self, vehicle_id):
        vehicle_make = get_one_vehicle(vehicle_id)[0]['make']
        vehicle_model = get_one_vehicle(vehicle_id)[0]['model']
        vehicle_plate_number = get_one_vehicle(vehicle_id)[0]['plate_number']
        db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).delete()
        db.session.commit()
        return {'message': f'Vehicle {vehicle_make} {vehicle_model} - {vehicle_plate_number} successfully deleted'}


class ChangeDriver(Resource):
    def patch(self, vehicle_id):
        if request.is_json:
            data = driver_id_parser.parse_args()
            vehicle_query = get_one_vehicle(vehicle_id)[0]['driver_id']
            if vehicle_query == data['driver_id']:
                db.session.query(Vehicle).filter(
                    Vehicle.id == vehicle_id).update({'driver_id': 0}, synchronize_session='fetch')
                db.session.commit()
                return {'message': f"Driver successfully got out of the car"}
            elif vehicle_query == 0:
                db.session.query(Vehicle).filter(
                    Vehicle.id == vehicle_id).update({'driver_id': data['driver_id']}, synchronize_session='fetch')
                db.session.commit()
                return {'message': f"Driver successfully got in the car"}
            else:
                db.session.query(Vehicle).filter(
                    Vehicle.id == vehicle_id).update({'driver_id': data['driver_id']}, synchronize_session='fetch')
                db.session.commit()
                return {'message': f"Driver successfully updated"}
        else:
            return {'error': 'The request payload is not in JSON format'}


api.add_resource(DriversList, "/drivers/driver/")
api.add_resource(DriverInfo, "/drivers/driver/<driver_id>/")
api.add_resource(VehiclesList, "/vehicles/vehicle/")
api.add_resource(VehicleInfo, "/vehicles/vehicle/<vehicle_id>/")
api.add_resource(ChangeDriver, "/vehicles/set_driver/<vehicle_id>/")


if __name__ == '__main__':
    app.run(debug=True)
