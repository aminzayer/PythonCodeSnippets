# Creating a Class:
# Define a simple Python class.
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return "Woof!"

# Inheritance:
# Create a subclass that inherits from a parent class.
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Encapsulation:
# Implement encapsulation by using private and public attributes.
class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute

    def area(self):
        return 3.14 * self.__radius * self.__radius

# Polymorphism:
# Demonstrate polymorphism with a common method name.
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    return animal.speak()

# Abstraction:
# Implement abstraction by defining an abstract base class.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Getter and Setter Methods:
# Use getter and setter methods for attribute access.
class Person:
    def __init__(self, name, age):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

# Composition:
# Create a class that is composed of other classes.
class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()

# Method Overloading:
# Implement method overloading using default arguments.
class Calculator:
    def add(self, a, b=0):
        return a + b

# Class Variables:
# Define and use class-level variables.
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

# Multiple Inheritance:
# Create a class that inherits from multiple parent classes.
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    pass
