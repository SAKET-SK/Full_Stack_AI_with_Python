# Return statements in functions
# A return statement is used to exit a function and return a value to the caller.
# Imagine you run a shop, what good is the use of your shop if you can't return the item asked by the customer?

def add(a, b):
    return a + b  # The function returns the sum of a and b

return_value = add(5, 3)  # Call the function and store the returned value
print("Returned Value:", return_value)  # Output: Returned Value: 8

# Return can actually return nothing. Simply meaning, Nothing -> implicitly returns "None" object, if you do not specify a return value.
# if I had used a print statement instead of return in the above function, the function would have printed the sum but returned None.

# -----

# Early return
def check_even(num):
    if num % 2 == 0:
        return True  # Return True if the number is even
    return False  # Return False if the number is odd

print(check_even(4))  # Output: True
print(check_even(7))  # Output: False

# Conclusion - A function can have multiple return statements, but only one will be executed based on the condition.

# -----

# Returning multiple values
def get_name_and_age():
    name = "Sagar"
    age = 25
    city = "Pune"
    return name, age, city  # Return multiple values as a tuple, can return anything, a number, a boolean, a list, a dictionary, an object, etc.

person_name, person_age, _ = get_name_and_age()  # Unpack the returned tuple
print(f"Name: {person_name}")  
print(f"Age: {person_age}")
# We can use _ (underscore) to ignore a value we don't need
