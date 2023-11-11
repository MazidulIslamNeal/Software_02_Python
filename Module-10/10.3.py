
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor request")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("Already at the top floor")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("Already at the bottom floor")
class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print(f"Invalid elevator number: {elevator_number}")
            return

        elevator = self.elevators[elevator_number - 1]
        print(f"\nRunning Elevator {elevator_number}...")
        elevator.go_to_floor(target_floor)

    def fire_alarm(self):
        print("\nFIRE ALARM ACTIVATED")
        for i, elevator in enumerate(self.elevators, start=1):
            print(f"Moving Elevator {i} to the bottom floor...")
            elevator.go_to_floor(self.bottom_floor)

# Testing the Building class
if __name__ == "__main__":
    # Creating a building with 2 elevators from 1st to 10th floor
    building = Building(bottom_floor=1, top_floor=10, num_elevators=2)

    # Running the elevators
    building.run_elevator(elevator_number=1, target_floor=5)
    building.run_elevator(elevator_number=1, target_floor=1)

    # Activating the fire alarm
    building.fire_alarm()
