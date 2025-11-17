# 3 ways to access base class: Code Duplication, Explicit Call and super()
# We will see how to access base class methods and attributes in derived class using these three methods.

# It all depends on the use case which method to use. Each one has its pros and cons.

# Base Class
class Engine:
    def __init__(self, type_, horsepower):
        self.type = type_
        self.horsepower = horsepower

class BikeEngine(Engine):
    def __init__(self, type_, horsepower, bike_type):
        # 1. Code Duplication: Directly initializing base class attributes
        self.type = type_
        self.horsepower = horsepower
        self.bike_type = bike_type

# In code duplication, you are repeating the code of base class in derived class.
# This can lead to maintenance issues if base class changes.

class CarEngine(Engine):
    def __init__(self, type_, horsepower, car_type):
        # 2. Explicit Call: Calling base class constructor directly, other values are initialized here.
        Engine.__init__(self, type_, horsepower)
        self.car_type = car_type

# This is better than code duplication, but still not ideal as it hardcodes the base class name.
# There is a better way of doing this using super().

class TruckEngine(Engine):
    def __init__(self, type_, horsepower, truck_type):
        # 3. Using super(): Calling base class constructor using super()
        super().__init__(type_, horsepower)
        self.truck_type = truck_type

# super() is more flexible and works well in multiple inheritance scenarios.
# It automatically resolves the base class and is less error-prone.
# Usually people prefer using super() in modern Python code. But there is no harm in explicit call if you are aware of its limitations.
