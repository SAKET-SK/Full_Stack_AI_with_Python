# Infinite Generators
# Generators can also be used to create infinite sequences, which can be very useful in certain scenarios.
# However, care must be taken when using infinite generators to avoid infinite loops. It can drain the memory if not handled properly.
# Useful for real time data streams, logging, simulations, etc.

def infinite_numbers():
    count = 1
    while True:  # Infinite loop
        yield count
        count += 1
        # The generator will keep yielding numbers indefinitely

generated_numbers = infinite_numbers()

for _ in range(10):  # Limiting to first 10 numbers for demonstration
    print(next(generated_numbers))  # Output: 1, 2, 3, ..., 10
