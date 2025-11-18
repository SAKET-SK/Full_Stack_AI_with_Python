# Handling Multiple Exceptions in Python
# This code demonstrates how to handle multiple exceptions using a single try block in Python.

def access_office_essentials(item, index):
    try:
        office_essentials = {"Laptop": 1, "Water Bottle": 2, "Notebook": 3, "Pen": 4}[item]   # [item] is a key lookup i.e., accessing the value for the given key
        priority = office_essentials * index  # Operator overloading happens, we need to typecast these 2 into integers
        print(f"Accessed {item} with priority {priority}.")
        print(f"Total cost is {priority}")
    except KeyError:
        print(f"Error: The item '{item}' does not exist in the office essentials dictionary.")
    except TypeError:
        print("Error: Index must be an integer.")

# Testing the function with different scenarios
access_office_essentials("Laptop", 2)        # Valid case
access_office_essentials("Tablet", 2)        # KeyError case
access_office_essentials("Notebook", "high") # TypeError case