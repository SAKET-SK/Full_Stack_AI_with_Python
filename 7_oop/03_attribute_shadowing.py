# Attribute shdowing
# In Python, if an instance attribute has the same name as a class attribute,
# the instance attribute will "shadow" or override the class attribute for that particular instance.

# Variable = Attribute inside class

class Animal:
    species = "Bear - The Generic Animal"  
    size = "Large" 

forest = Animal()
print(forest.species)  # Output: Bear - The Generic Animal

forest.species = "Panda"
print("After changing instance attribute: ",forest.species)  # Output: Panda
print("Accessing class attribute using class name: ",Animal.species)  # Output: Bear - The Generic Animal

del forest.species  # Deleting the instance attribute
print("After deleting instance attribute: ",forest.species)  # Output: Bear - The Generic Animal - falls back to class attribute
                    
