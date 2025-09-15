# Parameters and Arguments

message = "Hello, World!"
def greet(msg):
    print(msg)

greet(message)  # Call the function with an argument

# -----

arr = [1, 2, 3, 4, 5]

def edit_list(n):
    n[2] = 99  # Modify the third element of the list

edit_list(arr)  # Pass the list to the function
print(arr)  # The original list is modified

# -----

# Positional Arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("Amol", 30)  # Correct order - order is important
# display_info(30, "Amol")  # Incorrect order, would lead to wrong output
display_info(age=30, name="Amol")  # Using keyword arguments to avoid order issues

# -----

# args and kwargs
def special_offer(*items, **extras):
    print("Items:", items)  # items is a tuple of positional arguments
    print("Extras:", extras)  # extras is a dictionary of keyword arguments

special_offer("Laptop", "Mouse", discount=10, warranty="2 years")

# -----

# Default Parameters

# def number_list(order=[]):
#     n.append(100)  # Append 100 to the list
#     print(n)

def number_list(n=None):
    n.append(100)  # Append 100 to the list
    print(n)

number_list()  # Call without argument, n defaults to None and a new list is created
