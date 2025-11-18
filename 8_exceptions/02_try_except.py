# Try Except Example
# This code demonstrates how to handle exceptions using try and except blocks in Python.

office_essentials = {"Laptop": 1, "Water Bottle": 2, "Notebook": 3, "Pen": 4}

# office_essentials["Tablet"]  # This will raise a KeyError because "Tablet" key does not exist

try:
    office_essentials["Tablet"]
except KeyError:
    print("The item you are trying to access does not exist in the office essentials dictionary.")