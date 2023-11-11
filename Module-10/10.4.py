import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        self.current_speed = max(0, min(new_speed, self.max_speed))

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'Registration Number':<20} {'Max Speed (km/h)':<20} {'Current Speed (km/h)':<25} {'Travelled Distance (km)':<30}")
        for car in self.cars:
            print(f"{car.registration_number:<20} {car.max_speed:<20} {car.current_speed:<25} {car.travelled_distance:<30}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

# Create a list of 10 cars
cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

# Create a race named "Grand Demolition Derby" with a distance of 8000 kilometers
grand_demolition_derby = Race("Grand Demolition Derby", 8000, cars)

# Simulate the race progress
hours = 0
while not grand_demolition_derby.race_finished():
    grand_demolition_derby.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"Status after {hours} hours:")
        grand_demolition_derby.print_status()

# Print final status
print(f"\nFinal Status after {hours} hours:")
grand_demolition_derby.print_status()
