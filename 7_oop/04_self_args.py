# Self Arguments in Python
# In Python, the 'self' parameter in instance methods refers to the instance of the class itself.
# It allows access to the attributes and methods of the class in object-oriented programming.

class Dog:
    breed = "Labrador"

    def describe(self):
        return f"This dog is a {self.breed}."
    
info = Dog()
print(info.describe())  # Output: This dog is a Labrador.
print(Dog.describe(info))  # Output: This dog is a Labrador.

info2 = Dog()
info2.breed = "Beagle"
print(info2.describe())  # Output: This dog is a Beagle.

# Here, 'self' allows each instance to access its own attributes. 
# When we call describe() on different instances, 'self' refers to the respective instance, enabling instance-specific behavior.
# We can also call the method using the class name and passing the instance explicitly.