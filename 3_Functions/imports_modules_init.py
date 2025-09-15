# Python Imports, Modules, and __init__.py
# Imports allow you to use code from other modules (files) in your current script.
# A module is simply a file containing Python code (functions, classes, variables) that can be imported and used in other Python files.
# The __init__.py file is used to mark a directory as a Python package. It can be empty or can contain initialization code for the package.

# dunders ( __something__ )
# Dunder methods (short for "double underscore") are special methods in Python that have double underscores at the beginning and end of their names. They are also known as "magic methods" or "special methods."
# Dunder methods allow you to define the behavior of your objects for built-in operations, such as arithmetic operations, comparisons, and type conversions.
# For example, the __init__ method is a dunder method that initializes a new object when it is created.

# Example of importing a module and using a function from it
import math  # Importing the built-in math module
print(math.sqrt(16))  # Using the sqrt function from the math module, Output: 4.0

# Example of creating and using a custom module
# Assuming we have a file named my_module.py with the following content:
# def greet(name):
#     return f"Hello, {name}!"  
# We can import and use it as follows:
import my_module  # Importing the custom module
print(my_module.greet("Alice"))  # Using the greet function from my_module, Output: Hello, Alice!
# Note: Ensure that my_module.py is in the same directory as this script or in the Python path.

# Example of using __init__.py to create a package
# Assuming we have a directory structure like this:
# my_package/
# ├── __init__.py
# └── my_module.py
# The __init__.py file can be empty or contain initialization code for the package.
# We can import the package and use the module as follows:
from my_package import my_module  # Importing the module from the package
print(my_module.greet("Bob"))  # Using the greet function from my_module in my_package, Output: Hello, Bob!
# Note: Ensure that the my_package directory is in the same directory as this script or in the Python path.

# Dunder methods example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
person = Person("Charlie", 30)
print(person)  # Output: Charlie, 30 years old (calls the __str__ method)
# In this example, the __init__ method initializes the Person object, and the __str__ method defines how the object is represented as a string when printed.
# Common dunder methods include:
# __init__: Initializes a new object.
# __str__: Returns a string representation of the object.
# __repr__: Returns a detailed string representation of the object, useful for debugging.
# __add__: Defines the behavior of the + operator.
# __len__: Defines the behavior of the len() function.
# There are many more dunder methods that you can implement to customize the behavior of your classes.
# Dunder methods are a powerful feature of Python that allows you to create classes that behave like built-in types.
# They enable operator overloading and provide a way to define custom behavior for your objects.    
