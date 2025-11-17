# Inheritance and Composition Example

# Inheritance allows a class to inherit attributes and methods from another class.
# Composition allows a class to contain instances of other classes as attributes.

# Just a simple Class
class Dog:
    def __init__(self, breed):
        self.breed = breed      # If you are creting a variable inside constructor, it is  going to be there later.

    def bark(self):
        print(f"The {self.breed} dog says Woof!")

# Inheriting from the Dog class, we saw syntax of inheritance here.
class Person(Dog):  # You only use parentheses when you are inheriting from another class.
    def pet_dog(self):
        print("Petting the dog...")

# Composition: Person has a Dog
# Here, PersonWithDog class contains an instance of Dog class.

class PersonWithDog:
        Dog_class = Dog

        def __init__(self):
             # Through this constructor, we are creating an instance of Dog class inside PersonWithDog class.
             self.dog = self.Dog_class("Street Indie")  # Creating an instance of Dog inside PersonWithDog

# Execution Steps i.e. where the variable will be passed and how the methods will be called.
# Step 1: Line 26, the value "Street Indie" is passed on to Dog Constructor.
# Step 2: Line 7, the value is assigned to self.breed variable.
# Step 3: Line 11, the bark method is called on the dog instance inside

        def play_ball_with_dog(self):
             print(f"Playing Ball fetch with {self.dog.breed} dog.")
             self.dog.bark()  # Calling the bark method of Dog class through the dog instance.

class DogGames(PersonWithDog):
     Dog_class = Person
     # There is no constructor here, so it will use the constructor of PersonWithDog class.

# If there is no constructor, the class will automatically create a default constructor.

# Creating instances to demonstrate inheritance and composition
Dog_info = PersonWithDog()
Dog_games = DogGames()

# Using the methods - both classes have access to Dog class methods through composition.
Dog_info.play_ball_with_dog()
Dog_games.play_ball_with_dog()

Dog_games.dog.pet_dog()  # Calling the pet_dog method from Person class through Dog instance in DogGames class.

# This section is bit of a confusion, but it is to demonstrate how inheritance and composition can work together.