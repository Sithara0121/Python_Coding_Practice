# --- Object-Oriented Programming (OOP) in Python ---

# Class Definition
class Dog:
    # Constructor to initialize object attributes
    def __init__(self, name, breed):
        self.name = name  # Attribute: name of the dog
        self.breed = breed  # Attribute: breed of the dog

    # Method to make the dog bark
    def bark(self):
        print(f"{self.name} says woof!")  # Output: Buddy says woof!

    # Method to display dog info
    def info(self):
        print(f"{self.name} is a {self.breed}.")  # Output: Buddy is a Golden Retriever.

# Creating an object (instance) of Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()  # Output: Buddy says woof!
dog1.info()  # Output: Buddy is a Golden Retriever.

# Inheritance Example
class Animal:
    def __init__(self, name):
        self.name = name  # Attribute: name of the animal

    def speak(self):
        print(f"{self.name} makes a sound")  # Output: Rex makes a sound

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")  # Output: Rex barks

dog2 = Dog("Rex")
dog2.speak()  # Output: Rex barks

# Encapsulation Example (Private attribute)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Attribute: owner of the bank account
        self.__balance = balance  # Private attribute: balance, private variables start with '__'

    def deposit(self, amount):
        self.__balance += amount  # Modifies the private balance attribute

    def get_balance(self):
        return self.__balance  # Returns the private balance

account = BankAccount("John", 1000)
account.deposit(500)  # Deposit amount
print(account.get_balance())  # Output: 1500 (balance after deposit)

# Polymorphism Example
class Cat:
    def speak(self):
        print("Meow")  # Output: Meow

# Function demonstrating polymorphism
def animal_sound(animal):
    animal.speak()  # Calls the speak method, which is overridden in each subclass

cat = Cat()
dog = Dog("Rex")
animal_sound(cat)  # Output: Meow
animal_sound(dog)  # Output: Rex barks

# Abstraction Example
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract method to be implemented by child classes

class Dog(Animal):
    def sound(self):
        print("Woof")  # Output: Woof

dog3 = Dog()
dog3.sound()  # Output: Woof

# --- Important OOP Concepts Explained ---

# 1. **Class**: A class defines the properties (attributes) and behaviors (methods) of an object.
#    - In the example, Dog is a class that represents a dog with certain attributes (name, breed) and behaviors (bark, info).
#
# 2. **Object**: An object is an instance of a class.
#    - `dog1` is an object (instance) of the Dog class.
#
# 3. **Constructor**: The __init__ method initializes the attributes of an object when it is created.
#    - In the example, __init__ initializes `name` and `breed` for a Dog object.
#
# 4. **Methods**: Functions defined within a class to represent behaviors of an object.
#    - `bark()` and `info()` are methods of the Dog class.
#
# 5. **Inheritance**: Inheritance allows one class (child class) to inherit attributes and methods from another class (parent class).
#    - `Dog` inherits from `Animal` and overrides the `speak()` method.
#
# 6. **Encapsulation**: Restricting direct access to some of an object's attributes. This is achieved by making attributes private using `__` (double underscore).
#    - `__balance` is a private attribute, and its value can only be accessed through methods like `deposit()` and `get_balance()`.
#
# 7. **Polymorphism**: The ability of different classes to use the same method name but implement it in different ways.
#    - The method `speak()` is used in both the `Cat` and `Dog` classes but with different implementations.
#
# 8. **Abstraction**: Hiding the implementation details and exposing only the essential features of an object.
#    - The `Animal` class is abstract, and the `sound()` method is defined as an abstract method, meaning it must be implemented by any subclass.

