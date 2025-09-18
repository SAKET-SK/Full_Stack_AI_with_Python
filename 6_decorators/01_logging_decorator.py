# Logging Decorator
from functools import wraps
def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f"Completed calling function '{func.__name__}'")
        return result
    return wrapper

@log_activity
def account_type(type, FD="no"):      # Can add any number of parameters here, no restriction
    print(f"Account type is: {type}, FD status: {FD}")

account_type("Savings")
