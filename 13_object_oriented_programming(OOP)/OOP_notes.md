# Object-Oriented Programming (OOP) in Python
- Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code in a reusable and organized way.

## Key Concepts
1. `Class:`A blueprint for creating objects.
````
class Person:
    pass
````
2. `Object:`An instance of a class.
````
p1 = Person()
````
3. `Attributes and Methods:`
- `Attributes:` Variables that store data. 
- `Methods:` Functions that operate on attributes.
````
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}"

p1 = Person("Alice", 30)
print(p1.greet())
````
4. `Encapsulation:` Hiding internal details and exposing only necessary parts via methods.
````
class Counter:
    def __init__(self):
        self.__count = 0  # private attribute

    def increment(self):
        self.__count += 1

    def get_count(self):
        return self.__count
````
5. `Inheritance:` One class can inherit from another.
````
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.speak())  # Woof!
````
6. `Polymorphism:` Different classes can define methods with the same name.
````
class Cat:
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    print(animal.speak())

animal_speak(Dog())  # Woof!
animal_speak(Cat())  # Meow!
````