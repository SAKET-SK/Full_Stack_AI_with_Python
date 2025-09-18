# Decorators are a way to modify or enhance functions or methods without changing their actual code.
# They are often used for logging, access control, instrumentation, and caching.

from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!") 

say_hello()
print(say_hello.__name__)  # Outputs: say_hello -> because of @wraps; if not, it would output 'wrapper'
