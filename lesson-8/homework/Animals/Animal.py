import time
import threading

class Animal:
    def __init__(self, name):
        self.name = name
        self.energy = 50
        self.is_sleeping = False

    def eat(self):
        if self.is_sleeping:
            print(f"{self.name} is sleeping and cannot eat right now.")
            return
        self.energy += 20
        print(f"{self.name} eats and gains energy. Energy: {self.energy}")

    def sleep(self, duration=5):
        if self.is_sleeping:
            print(f"{self.name} is already sleeping.")
            return

        self.is_sleeping = True
        print(f"{self.name} is now sleeping for {duration} seconds...")

        def wake_up():
            time.sleep(duration)
            self.is_sleeping = False
            print(f"{self.name} has woken up and is ready to work!")

        threading.Thread(target=wake_up, daemon=True).start()

class Cow(Animal):
    def produce_milk(self):
        if self.is_sleeping:
            print(f"{self.name} is sleeping and cannot produce milk.")
            return
        if self.energy < 40:
            print(f"{self.name} is too tired to produce milk.")
            return
        self.energy -= 40
        print(f"{self.name} produces 3 liters of milk. Energy: {self.energy}")

class Chicken(Animal):
    def lay_egg(self):
        if self.is_sleeping:
            print(f"{self.name} is sleeping and cannot lay an egg.")
            return
        if self.energy < 15:
            print(f"{self.name} is too tired to lay an egg.")
            return
        self.energy -= 15
        print(f"{self.name} lays an egg. Energy: {self.energy}")

class Sheep(Animal):
    def produce_wool(self):
        if self.is_sleeping:
            print(f"{self.name} is sleeping and cannot produce wool.")
            return
        if self.energy < 80:
            print(f"{self.name} hasn't grown enough wool yet.")
            return
        self.energy -= 40
        print(f"{self.name} produces wool. Energy: {self.energy}")
