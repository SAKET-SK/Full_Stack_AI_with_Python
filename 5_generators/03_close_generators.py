# Yeild From & Close Generators
# The yield from statement is used to delegate part of a generator's operations to another generator.
# It allows a generator to yield all values from another iterable (like a list, tuple, or another generator) without having to write an explicit loop.
# This can simplify code and improve readability when dealing with nested generators or when you want to yield
# all values from a sub-generator.

# The close() method is used to stop a generator. When close() is called, a GeneratorExit exception is raised inside the generator to terminate it.
# This is useful when you want to clean up resources or stop the generator from producing more values.
# If the generator is already exhausted, calling close() has no effect.

def local_fruits():
    yield "Apple"
    yield "Banana"
    yield "Cherry"

def imported_fruits():
    yield "Mango"
    yield "Pineapple"
    yield "Dragonfruit"

def all_fruits():
    yield from local_fruits()  # Delegating to local_fruits generator
    yield from imported_fruits()  # Delegating to imported_fruits generator

for fruit in all_fruits():
    print(fruit)

# Try - Except

def fruit_stall():
    try:
        while True:
            fruit_request = yield "Packing your fruit..."
    except:
        print("Stall is closed. No more fruits can be served.")

stall = fruit_stall()
print(next(stall))  # Start the generator
stall.close()  # Close the generator, triggering the except block. Clean up code runs here.
