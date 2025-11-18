# File Handling in Python
# This code demonstrates how to handle file operations and exceptions in Python.

file = open("demo.txt", "w")  # Open a file in write mode
try:
    file.write("This is a demo file for exception handling in Python.\n")
finally:
    file.close()  # Ensure the file is closed after writing

# If you dont want to use try-catch, python provides a better way using 'with' statement

with open("demo.txt", "w") as file:  # Open a file in read mode
    file.write("Using 'with' statement to handle files is better.\n")  

# behind the scenes, when you create the reference, it invoke __enter__ method i.e. file.__enter__()
# and when the block is exited, it invokes __exit__ method to close the file automatically i.e. file.__exit__()

# using with actually calls all these dunders for you automatically, unlike the first example where you have to manually load and close the file.