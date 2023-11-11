class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.kilometer_counter = 0

    def drive(self, hours, speed):
        self.kilometer_counter += hours * speed

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

# Creating an electric car and a gasoline car
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

# Driving the cars
electric_car.drive(3, 120)  # Drive at 120 km/h for 3 hours
gasoline_car.drive(3, 100)  # Drive at 100 km/h for 3 hours

# Printing out kilometer counters
print(f"Electric Car Kilometer Counter: {electric_car.kilometer_counter} km")
print(f"Gasoline Car Kilometer Counter: {gasoline_car.kilometer_counter} km")
