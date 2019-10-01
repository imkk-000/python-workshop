from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def description(self):
        pass

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Static method
    @staticmethod
    def split_name(name):
        return name.spilt()

    # Class method
    @classmethod
    def from_string(cls, name_age_str):
        name, age = map(str, name_str.split(' '))
        dog = cls(name, age)
        return dog

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    # instance method
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return F"{self.name} is walking!"

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs super fast {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def run(self, speed):
        return super().run(speed)

# Group of Pets
class Pets():
    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))
