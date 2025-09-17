# Generators are a simple and powerful tool for creating iterators.
# They are written like regular functions but use the yield statement whenever they want to return data.
# Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).

# They look exactly like regular functions but use the yield statement whenever they want to return data.

def serve_food():
    yield "Plate 1: Chicken"
    yield "Plate 2: Sandwich"
    yield "Plate 3: Salad"
    yield "Plate 4: Pasta"
    yield "Plate 5: Fish"

table = serve_food()  # This creates a generator object, it is not executed yet. Like a reference to above function.

for plate in table:
    print(plate)

# next() function can be used to manually iterate through the generator

table = serve_food()  # Create a new generator object
print(next(table))  # Output: Plate 1: Chicken
print(next(table))  # Output: Plate 2: Sandwich
print(next(table))  # Output: Plate 3: Salad
print(next(table))  # Output: Plate 4: Pasta
print(next(table))  # Output: Plate 5: Fish
# print(next(table))  # Uncommenting this line will raise StopIteration error as there are no more items to yield

# Generators can be more memory efficient than lists, especially for large datasets, as they generate items on-the-fly and do not store the entire list in memory.
# Amazing to see that how it keeps track of its state between successive calls to next().
