# metaclasses
# Control how classes instantiate objects
# Factory pattern
# singleton pattern
# Frameworks like djnago and sqlalchmey
# Python itself uses this in the code:Enum

#Types and classes
# - In Python, everything is an object, including classes and types.
# - each object has a type, indicating its nature
# the type() functions tells you an object's types

cats = ["tiger", "lion", "cheetah"]
print(type(cats))
print(type(cats[0][2]))

class Dog:
    pass
print(type(Dog()))

max([1, 2, 3])
type(max)

from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
print(type(Color.RED))
print(type(Color.RED.value))

#let's get meta
print(type(Color))
print(type(Enum))

from enum import EnumType
print(type(EnumType))
print(type(Dog))
print(type(type))

# Dynamic classes
# Creating Classes
# Classes themselves are objects
# the mechanism that creates classes is called metaclass
# the type() function can be used to construct a class

class Dessert:
    pass

sundae = Dessert()
print(type(sundae))
print(type(Dessert))

# The type() function can be used to create a class
Appetizer = type("Appetizer", (object,), {"name": "Salad", "calories": 200})
shrimp = Appetizer()
print(type(shrimp))
print(type(Appetizer))
print(type(Appetizer()))
# here we have created a class called Appetizer with a name and calories attribute
# the type() function takes three arguments:
# 1. The name of the class
# 2. A tuple of base classes (in this case, object)
# 3. A dictionary of attributes and methods
# The type() function can also be used to create a class with methods


print("-----------------")# Creating a class with methods
Dip = type("Dip", (Appetizer,), {"name": "Guacamole", "calories": 150, "serve": lambda self: print("Serve with chips")})
guacamole = Dip()
print(type(guacamole))
print(type(Dip))
print(type(Dip()))
print(guacamole.name)
print(guacamole.calories)
print(guacamole.serve())


def to_string(obj):
    return f"OnToast(toppings=f{obj.toppings})"

OnToast = type("OnToast", (Appetizer,), {"toppings": ["Avocado", "Tomato"], "__str__": to_string})
avocado_toast = OnToast()
print(type(avocado_toast))
print(type(OnToast))
print(type(OnToast()))
print(avocado_toast.toppings)
print(avocado_toast.__str__())
print(avocado_toast)

#invoking things
#  you can create an invokable things with the __call__ method
# Allows you to call pbjects like functions

import subprocess
class Action:
    def __init__(self, actions):
        self.actions = actions

    def do_it(self):
        for action in self.actions:
            subprocess.run(action, shell=True)

# subprocess runs takes a list of actions, the first item in the list is the command to run
# and the rest are the arguments to the commands

hellos = Action(["echo hello", "echo world"])
hellos.do_it()
print(hellos.actions)

class Action:
    def __init__(self, actions):
        self.actions = actions

    def __call__(self):
        for action in self.actions:
            subprocess.run(action, shell=True)
hellos = Action(["echo hello", "echo world"])
hellos()

# The __call__ method allows you to call the object like a function

# Paranthesis invoke
# Paranthesis cause an object to be called
# Evereything in python is an object

print
print()

# objects creations is invocation
# classes are objects
# instantiating an object from a class uses parenthesis on the class
# class is a callable
# class is inherited from the type metaclass
# the type metaclass has a __call__ method
# the __call__() method invokes __new()__ and __init__()__ methods
# default methods for __new__() and __init__()__ are defined in the type metaclass
# __new__() is responsible for creating the object
# __init__()__ is responsible for initializing the object

def new(cls):
    print("Creating a new instance of", cls.__name__)
    obj = object.__new__(cls)
    obj.description = "Amuse your mouth"
    return obj

AmuseBouche = type("AmuseBouche", (object,), {"__new__": new})
amuse = AmuseBouche()
print(amuse.description)

#Class Creation is invocation
# The __new__ method is responsible for creating the object
# what if you want to do something when a class is created?
# Cannot override type.__new__ method
# class inheritance syntax allow for a metaclass argument
# Create a special class that inherits from type
# Override __new__() on that class
# Use the special metaclass when declaring another class

class CounterMeta(type):
    count = 0
    def __new__(cls, name, bases, attrs):
        print("Creating a new class:", name)
        kls= super().__new__(cls, name, bases, attrs)
        cls.count += 1
        return kls

class Pie(metaclass=CounterMeta):
    pass

apple = Pie()
rassberry = Pie()
apple.__class__.count














