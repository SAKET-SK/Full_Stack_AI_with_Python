# Property Decorators in Python
# Property decorators allow you to define methods in a class that can be accessed like attributes.

class Tree:
    def __init__(self, age):
        self._age = age  # Using a leading underscore to indicate that this is a "private" variable.

    @property           # Also called getter
    def age(self):
        return self._age + 2  # Adding 2 years to the actual age for some reason.
    
    # The @property decorator allows us to access the age method like an attribute.

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

Tree_Age = Tree(5)
print(Tree_Age.age)  # Accessing age like an attribute, Output: 7

# We control everything through the property decorators. i.e. how we want to read the value and how we want to edit those values

