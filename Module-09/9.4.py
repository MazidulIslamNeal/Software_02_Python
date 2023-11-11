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

# Create a list of 10 cars
cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

# Race loop
race_finished = False
while not race_finished:
    for car in cars:
        # Change speed by a random value between -10 km/h and +15 km/h
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)

        # Drive for one hour
        car.drive(1)

        # Check if any car has advanced at least 10,000 kilometers
        if car.travelled_distance >= 10000:
            race_finished = True
            break

# Print out the properties of each car in a formatted table
print(f"{'Registration Number':<20} {'Max Speed (km/h)':<20} {'Current Speed (km/h)':<25} {'Travelled Distance (km)':<30}")
for car in cars:
    print(f"{car.registration_number:<20} {car.max_speed:<20} {car.current_speed:<25} {car.travelled_distance:<30}")
