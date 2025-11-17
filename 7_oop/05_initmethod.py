# init method example
# The __init__ method in Python is a special method that is called when an instance (object) of a class is created.
# It is used to initialize the attributes of the class.

# Simply putting, you are creating a consrtuctor via __init__ method.

class Person:
    def __init__(self, type_, shirt_size):
        self.type = type_
        self.shirt_size = shirt_size 

        # type is an operator in Python, so we use type_ to avoid conflict.
        # Sometimes you want to use variable names that make sense but they might conflict with reserved words in Python.
        # So this is a common practice in many production systems to add an underscore at the end of such variable names. 

        # The variables have not been declared before, but we are creating them on the fly.
        # This is possible because of the constructor method __init__.

    def display_info(self):
        return f"Type: {self.type}, Shirt Size: {self.shirt_size}"

# Creating instances of the Person class
info1 = Person("Formals", "L")
print(info1.display_info())

info2 = Person("Casuals", "M")
print(info2.display_info())
