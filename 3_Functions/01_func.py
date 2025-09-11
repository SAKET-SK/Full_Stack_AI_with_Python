# Reducing code duplication with functions
# Functions allow us to encapsulate reusable code blocks.
# Instead of repeating the same code multiple times, we can define a function and call it whenever needed.

# PROBLEM STATEMENT: You own a place and many people come to stay; checking in and out. You want keep a track.
# TO DO: Write a guest greet function. Call it multiple times for different guests.
# Example : greet(name, room_number)

def greet(name, room_number):   # Function definition with parameters
    print(f"Hello {name}, welcome to your room number {room_number}. Enjoy your stay!")

# Calling the function for different guests
greet("Alice", 101)      # Function call with arguments
greet("Bob", 202)
greet("Charlie", 303)
