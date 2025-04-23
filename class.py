class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self._power = power
        self.strength_level = strength_level

    def introduce(self):
        print(f"I'm {self.name}, and I use {self._power}!")

    def power_up(self):
        self.strength_level += 10
        print(f"{self.name} is powering up! Strength: {self.strength_level}")

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength_level, flight_speed):
        super().__init__(name, power, strength_level)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")

print("Create your superhero!")
name = input("Enter name: ")
power = input("Enter power: ")
strength = int(input("Enter strength level (0-100): "))
can_fly = input("Can your hero fly? (yes/no): ").lower()

if can_fly == "yes":
    speed = int(input("Enter flight speed in km/h: "))
    hero = FlyingSuperhero(name, power, strength, speed)
    hero.introduce()
    hero.power_up()
    hero.fly()
else:
    hero = Superhero(name, power, strength)
    hero.introduce()
    hero.power_up()
