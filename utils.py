import random
from datetime import datetime

from models import Driver, Vehicle

letters = ['AA', 'KА', 'AB', 'KB', 'AC', 'KC', 'AE', 'KE', 'AH', 'KH', 'AI', 'KI',
           'AM', 'KM', 'AO', 'KO', 'AP', 'KP', 'AT', 'KT', 'AX', 'KX', 'BA', 'HA',
           'BB', 'HB', 'BC', 'HC', 'BE', 'HE', 'BH', 'HH', 'BI', 'HI', 'BK', 'HK',
           'BM', 'HM', 'BO', 'HO', 'BT', 'HT', 'BX', 'HX', 'CA', 'IA', 'CB', 'IB',
           'CE', 'IE']

symbols = 'ABCEHIKMOPTXO'


def generate_plate_number():
    first_letters = random.choice(letters)
    numbers = random.randint(pow(10, 3), (pow(10, 4) - 1))
    last_letters = f'{random.choice(symbols)}{random.choice(symbols)}'
    plate_number = f'{first_letters} {numbers} {last_letters}'
    return plate_number


def get_one_driver(driver_id):
    driver_query = Driver.query.filter(Driver.id == driver_id)
    result = [
        {
            'id': driver.id,
            'first_name': driver.first_name,
            'last_name': driver.last_name,
            'created_at': driver.created_at.strftime("%d/%m/%Y %H:%M:%S"),
            'update_at': driver.updated_at.strftime("%d/%m/%Y %H:%M:%S"),
        } for driver in driver_query]
    return result


def get_all_drivers():
    driver_query = Driver.query.all()
    result = [
        {
            'id': driver.id,
            'first_name': driver.first_name,
            'last_name': driver.last_name,
            'created_at': driver.created_at.strftime("%d/%m/%Y %H:%M:%S"),
            'update_at': driver.updated_at.strftime("%d/%m/%Y %H:%M:%S"),
        } for driver in driver_query]
    return result


def get_drivers_create_after_date(created_at__gte):
    driver_query = Driver.query.filter(Driver.created_at >= datetime.strptime(created_at__gte, "%d/%m/%Y"))
    result = [
        {
            'id': driver.id,
            'first_name': driver.first_name,
            'last_name': driver.last_name,
            'created_at': driver.created_at.strftime("%d/%m/%Y"),
            'update_at': driver.updated_at.strftime("%d/%m/%Y"),
        } for driver in driver_query]
    return result


def get_drivers_create_before_date(created_at__lte):
    driver_query = Driver.query.filter(Driver.created_at < datetime.strptime(created_at__lte, "%d/%m/%Y"))
    result = [
        {
            'id': driver.id,
            'first_name': driver.first_name,
            'last_name': driver.last_name,
            'created_at': driver.created_at.strftime("%d/%m/%Y"),
            'update_at': driver.updated_at.strftime("%d/%m/%Y"),
        } for driver in driver_query]
    return result


def get_one_vehicle(vehicle_id):
    vehicle_query = Vehicle.query.filter(Vehicle.id == vehicle_id)
    result = [
        {
            'id': vehicle.id,
            'driver_id': vehicle.driver_id,
            'make': vehicle.make,
            'model': vehicle.model,
            'plate_number': vehicle.plate_number,
            'created_at': vehicle.created_at.strftime("%d/%m/%Y %H:%M:%S"),
            'update_at': vehicle.updated_at.strftime("%d/%m/%Y %H:%M:%S"),
        } for vehicle in vehicle_query]
    return result


def get_vehicle_with_driver():
    vehicle_query = Vehicle.query.filter(Vehicle.driver_id != 0)
    result = [
        {
            'id': vehicle.id,
            'driver_id': vehicle.driver_id,
            'make': vehicle.make,
            'model': vehicle.model,
            'plate_number': vehicle.plate_number,
            'created_at': vehicle.created_at.strftime("%d/%m/%Y %H:%M:%S"),
            'update_at': vehicle.updated_at.strftime("%d/%m/%Y %H:%M:%S"),
        } for vehicle in vehicle_query]
    return result


def get_vehicle_without_driver():
    vehicle_query = Vehicle.query.filter(Vehicle.driver_id == 0)
    result = [
        {
            'id': vehicle.id,
            'driver_id': vehicle.driver_id,
            'make': vehicle.make,
            'model': vehicle.model,
            'plate_number': vehicle.plate_number,
            'created_at': vehicle.created_at.strftime("%d/%m/%Y %H:%M:%S"),
            'update_at': vehicle.updated_at.strftime("%d/%m/%Y %H:%M:%S"),
        } for vehicle in vehicle_query]
    return result


def get_all_vehicle():
    vehicle_query = Vehicle.query.all()
    result = [
        {
            'id': vehicle.id,
            'driver_id': vehicle.driver_id,
            'make': vehicle.make,
            'model': vehicle.model,
            'plate_number': vehicle.plate_number,
            'created_at': vehicle.created_at.strftime("%d/%m/%Y %H:%M:%S"),
            'update_at': vehicle.updated_at.strftime("%d/%m/%Y %H:%M:%S"),
        } for vehicle in vehicle_query]
    return result


def replace_symbol_in_string(tmp_str):
    result = ''
    for i in tmp_str:
        if i == '-':
            i = "/"
            result += i
        else:
            result += i
    return result
