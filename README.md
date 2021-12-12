# Cars park
REST APIs project with Python and Flask

---

### Description

---
This is REST APIs for cars park with drivers.

---

### How to use

---
Driver's info:
- **GET** */drivers/driver/* - output a list of drivers
- **GET** */drivers/driver/?created_at__gte=10-11-2021* - output a list of drivers,
  that created after 10-11-2021
- **GET** */drivers/driver/?created_at__lte=16-11-2021* - output a list of drivers,
  that created until 16-11-2021
- **GET** */drivers/driver/<driver_id>/* - get information about the driver
- **POST** */drivers/driver/* - create new driver
- **UPDATE** */drivers/driver/<driver_id>/* - edit driver
- **DELETE** */drivers/driver/<driver_id>/* - delete driver

Vehicle's info:
- **GET** */vehicles/vehicle/* - output a list of vehicles
- **GET** */vehicles/vehicle/?with_drivers=yes* - output a list of vehicles with drivers
- **GET** */vehicles/vehicle/?with_drivers=no* - output a list of vehicles without drivers
- **GET** */vehicles/vehicle/<vehicle_id>* - get information about the vehicle
- **POST** */vehicles/vehicle/* - create new vehicle
- **UPDATE** */vehicles/vehicle/<vehicle_id>/* - edit vehicle
- **POST** */vehicles/set_driver/<vehicle_id>/* - driver gets in the car / driver gets out of the car  
- **DELETE** */vehicles/vehicle/<vehicle_id>/* - delete vehicle

---

### Project environment

---
[requirements.txt](./requirements.txt)

---

### Project setup

---
[SETUP.md](./SETUP.md)
