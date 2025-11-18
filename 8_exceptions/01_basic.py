# Basics of Exception Handling in Python
# When something goes wrong, even if you don't expect it to, Python raises an exception.
# You do not crash or scrap the entire python program; instead you handle the exceptions gracefully.

office_essentials = ["Laptop", "Water Bottle", "Notebook", "Pen"]

print(office_essentials[4])  # This will raise an IndexError because index 4 does not exist

# Types of Errors we might encounter:
# 1. IndexError - Accessing the index which does not exist in a list
# 2. KeyError - Accessing a key which does not exist in a dictionary
# 3. ZeroDivisionError - Dividing a number by zero
# 4. TypeError - Performing an operation on incompatible data types
# 5. NameError - Using a variable that has not been defined

# And many more...