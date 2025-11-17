# Namespaces in Python are implemented using modules and packages.
# A namespace is a container that holds a set of identifiers (names) and ensures that all the names are unique within that container.

class Animal:
    species = "Bear - The Generic Animal"   # When variable goes inside the class, it becomes properties of the class

print(Animal.species)  # Output: Generic Animal

Animal.is_bear = True  # Dynamically adding a new property to the class
print(Animal.is_bear)  # Output: True

forest = Animal()  # Creating an instance of the Animal class
print(forest.species)  # Output: Bear - The Generic Animal
print(forest.is_bear)  # Output: True

# Both the class and its instance share the same namespace for class variables and methods.

forest.is_bear = False  # Changing the property of object - will this be same in class?

print(Animal.is_bear)  # From Class - Output: True
print(forest.is_bear)  # From Instance -  Output: False

# The instance 'forest' now has its own 'is_bear' property that shadows the class property.

forest.vegetation = "Alpine Trees"  # Adding a new property to the instance - but this won't be in class
# print(Animal.vegetation)  # This would raise an AttributeError
print(forest.vegetation)  # Output: Alpine Trees

# This demonstrates how namespaces work in Python, with classes and instances maintaining their own separate namespaces for attributes.