# Documenting your functions
# Documenting your functions is crucial for code readability and maintainability. It helps others (and your future self) understand what the function does, its parameters, and its return values.

def multiply(a, b):
    """
    Multiplies two numbers and returns the result.

    Parameters:
    a (int, float): The first number to multiply.
    b (int, float): The second number to multiply.

    Returns:
    int, float: The product of a and b.
    """
    return a * b

result = multiply(4, 5)
print("Multiplication Result:", result)  # Output: Multiplication Result: 20
print(multiply.__doc__)  # Accessing the docstring of the function
help(multiply)  # Using help() to get the documentation of the function
# Using docstrings is a good practice to document your functions. It provides a clear understanding of the function's purpose and usage.
# Docstrings are written using triple quotes (""" or ''') and can span multiple lines.
# The first line is a brief description of the function.
# The following lines can provide more details about parameters, return values, and any exceptions raised.
# You can access the docstring of a function using the __doc__ attribute or the help() function.
# Tools like Sphinx can be used to generate documentation from docstrings automatically.
# Proper documentation is especially important in larger projects or when working in teams, as it facilitates collaboration and code maintenance.

# -----

# Built-in Functions
# Python provides several built-in functions that are always available for use. Some commonly used built-in functions include:
# abs(): Returns the absolute value of a number.
print(abs(-10))  # Output: 10
# len(): Returns the length of an object (like a string, list, tuple, etc.).
print(len("Hello"))  # Output: 5
# max(): Returns the largest item in an iterable or the largest of two or more arguments.
print(max(1, 5, 3))  # Output: 5
# min(): Returns the smallest item in an iterable or the smallest of two or more arguments.
print(min(1, 5, 3))  # Output: 1
# sum(): Sums the items of an iterable from left to right and returns the total.
print(sum([1, 2, 3, 4]))  # Output: 10
# round(): Rounds a floating-point number to the nearest integer or to a specified number of decimal places.
print(round(3.14159, 2))  # Output: 3.14
# type(): Returns the type of an object.
print(type(42))  # Output: <class 'int'>
# str(), int(), float(): Convert values to string, integer, and float types respectively.
print(str(100))  # Output: '100'
print(int("100"))  # Output: 100    
print(float("3.14"))  # Output: 3.14
# list(), tuple(), set(), dict(): Convert values to list, tuple, set, and dictionary types respectively.
print(list((1, 2, 3)))  # Output: [1, 2, 3]
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}
print(dict([("a", 1), ("b", 2)]))  # Output: {'a': 1, 'b': 2}
# range(): Generates a sequence of numbers, commonly used in for loops. 
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]
# enumerate(): Adds a counter to an iterable and returns it as an enumerate object.
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
# Output:
# 0 a       
# 1 b
# 2 c
# zip(): Combines multiple iterables (like lists or tuples) into a single iterable of tuples.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# map(): Applies a function to all items in an iterable and returns a map object (which can be converted to a list or other iterables).
squared = map(lambda x: x**2, [1, 2, 3])
print(list(squared))  # Output: [1, 4, 9]
# filter(): Filters items in an iterable based on a function that returns True or False.
even_numbers = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print(list(even_numbers))  # Output: [2, 4, 6]
