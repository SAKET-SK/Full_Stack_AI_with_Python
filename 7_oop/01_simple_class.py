# Object Oriented Programming: Simple Class Example
# Class - A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

class Dog:
    pass

print(type(Dog))  # Output: <class 'type'> 
# But remember, everything in Python is an object, including classes themselves!

labrador = Dog()
print(type(labrador))  # Output: <class '__main__.Dog'>
# Here, we created an instance of the Dog class named labrador.

print(type(labrador) is Dog)  # Output: True
# This confirms that labrador is indeed an instance of the Dog class.