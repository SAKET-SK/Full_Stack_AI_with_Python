# nonlocal vs global
# nonlocal is used to work with variables inside nested functions, where the variable should not belong to the inner function.
# Use the nonlocal keyword to declare that a variable inside a nested function (inner function)
# refers to a variable in the nearest enclosing scope (excluding globals).

def update_counter():
    counter_type = "Public-Relations"
    def bank():
        nonlocal counter_type  # Declare that we want to use the nearest enclosing scope's counter_type
        counter_type = "Premium"  # Modify the enclosing scope variable
        print(f"Inside bank function:- {counter_type}")
    bank()  # Call the inner function

update_counter()  # Call the outer function
# The above will print "Inside bank function:- Premium" because the inner function modified the enclosing scope variable.
# However, since we did not print counter_type outside the inner function, we cannot see its value here.
# If we try to print counter_type here, it will raise an error because counter_type is not defined in this scope.
# print(f"Outside both functions:- {counter_type}")  # This would raise an error

# If you comment out the nonlocal line, the inner function will create a new local variable named counter_type,
# and the enclosing scope variable will remain unchanged.

def new_counter():
    def new_cabin():
        global counter_type
        counter_type = "Standard"  # This will create or modify a global variable
        print(f"Inside new_cabin function:- {counter_type}")
    new_cabin()  # Call the inner function
new_counter()  # Call the outer function
print(f"Outside both functions:- {counter_type}")  # This will print "Outside both functions:- Standard"
# The above will print "Inside new_cabin function:- Standard" and "Outside both functions:- Standard"
# because the inner function modified the global variable.
