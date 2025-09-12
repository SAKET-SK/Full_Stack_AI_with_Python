# Scopes and name resolution in Python

# LEGB Rule: Local, Enclosing, Global, Built-in

# Local scope: Names defined within a function
# Enclosing scope: Names in the local scope of any and all enclosing functions
# Global scope: Names defined at the top level of a module or declared global within a def
# Built-in scope: Names preassigned in the built-in names module

def account_type():
    account = "Savings"  # Local scope
    print(f"Inside account_type function:- {account}")

account = "Personal"  # Global scope
account_type()  # Call the function again to see local scope does not affect global
print(f"Outside the function:- {account}")

def bank_counter():
    counter_type = "Premium"  # Enclosing scope
    def inner_counter():
        counter_type = "Standard"  # Enclosing scope
        print(f"Inside inner_counter function:- {counter_type}")
    inner_counter()  # Call the inner function
    print(f"Outside inner_counter but inside bank_counter:- {counter_type}")

counter_type = "Basic"  # Global scope
bank_counter()  # Call the outer function
print(f"Outside both functions:- {counter_type}")
