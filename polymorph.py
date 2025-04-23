class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

print("\nChoose a vehicle to move:")
print("1. Car\n2. Plane\n3. Boat")
choice = input("Enter number: ")

if choice == "1":
    vehicle = Car()
elif choice == "2":
    vehicle = Plane()
elif choice == "3":
    vehicle = Boat()
else:
    print("Invalid choice.")
    vehicle = None

if vehicle:
    vehicle.move()
