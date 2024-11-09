"""
Liskov Substitution Principle
Is a principle in object-oriented programming that states that objects of a superclass shall be replaceable with objects of its subclasses without breaking the application.
"""

# Base class
class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying")

# Derived class
class Ostrich(Bird):
    def fly(self):
        print(f"{self.name} can't fly")

# Derived class
class Sparrow(Bird):
    def fly(self):
        print(f"{self.name} is flying")

# Derived class that violates the Liskov Substitution Principle
class Penguin(Bird):
    def fly(self):
        raise Exception(f"{self.name} can't fly")

if __name__ == "__main__":
    bird = Bird("Bird")
    bird.fly()

    ostrich = Ostrich("Ostrich")
    ostrich.fly()

    penguin = Penguin("Penguin")
    penguin.fly()