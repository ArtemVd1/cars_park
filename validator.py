from flask_restful import reqparse


driver_parser = reqparse.RequestParser()
vehicle_parser = reqparse.RequestParser()
driver_id_parser = reqparse.RequestParser()


def strict_str_validator(data):
    if isinstance(data, str):
        return data
    else:
        raise TypeError(f'Wrong type:{type(data)}')


driver_parser.add_argument('first_name',
                           type=strict_str_validator,
                           required=True,
                           help='First name: {error_msg}')

driver_parser.add_argument('last_name',
                           type=strict_str_validator,
                           required=True,
                           help='Last name: {error_msg}')

vehicle_parser.add_argument('driver_id',
                            type=int,
                            required=True,
                            help="Driver's id: {error_msg}")

vehicle_parser.add_argument('make',
                            type=str,
                            required=True,
                            help='Vehicle make: {error_msg}')

vehicle_parser.add_argument('model',
                            type=str,
                            required=True,
                            help="Vehicle's model: {error_msg}")

vehicle_parser.add_argument('plate_number',
                            type=str,
                            required=True,
                            help="Vehicle's plate_number: {error_msg}")

driver_id_parser.add_argument('driver_id',
                              type=int,
                              required=True,
                              help="Driver's id: {error_msg}")
