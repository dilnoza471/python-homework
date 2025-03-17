from Animals.Animal import *

class Farm:
    def __init__(self):
        self.animals = [
            Cow("Bessie the Cow"),
            Chicken("Cluck the Chicken"),
            Sheep("Jay the Sheep")
        ]
    def show_animals(self):
        print("\nAnimals on the farm:")
        for idx, animal in enumerate(self.animals):
            status = "Sleeping" if animal.is_sleeping else "Awake"
            print(f"{idx + 1}. {animal.name} (Energy: {animal.energy}, Status: {status})")

    def interact(self):
        while True:
            self.show_animals()
            print("\nOptions:")
            print("1. Feed an animal")
            print("2. Put an animal to sleep")
            print("3. Collect resources (milk/eggs)")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.feed_animal()
            elif choice == "2":
                self.sleep_animal()
            elif choice == "3":
                self.collect_resources()
            elif choice == "4":
                print("Goodbye, Farmer!")
                break
            else:
                print("Invalid choice. Try again.")

    def feed_animal(self):
        animal = self.select_animal()
        if animal:
            animal.eat()

    def sleep_animal(self):
        animal = self.select_animal()
        if animal:
            duration = int(input("Enter sleep duration (seconds): "))
            animal.sleep(duration)

    def collect_resources(self):
        animal = self.select_animal()
        if isinstance(animal, Cow):
            animal.produce_milk()
        elif isinstance(animal, Chicken):
            animal.lay_egg()
        elif isinstance(animal, Sheep):
            animal.produce_wool()
        else:
            print("This animal does not produce resources.")

    def select_animal(self):
        self.show_animals()
        try:
            choice = int(input("Select an animal (number): ")) - 1
            if 0 <= choice < len(self.animals):
                return self.animals[choice]
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    farm = Farm()
    farm.interact()