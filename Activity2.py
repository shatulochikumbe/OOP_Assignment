class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves in a generic way.")

class Dog(Animal):
    def move(self):
        print(f"{self.name} runs and barks: Woof!")

class Fish(Animal):
    def move(self):
        print(f"{self.name} swims in the water.")

class Bird(Animal):
    def move(self):
        print(f"{self.name} flies through the air.")

# Example usage:
animal = Animal("Generic Animal")
dog = Dog("Buddy")
fish = Fish("Nemo")
bird = Bird("Tweety")

animal.move()
dog.move()
fish.move()
bird.move()

# Demonstrate polymorphism with a list:
animals = [animal, dog, fish, bird]
for creature in animals:
    creature.move()  # The correct move() method is called for each object