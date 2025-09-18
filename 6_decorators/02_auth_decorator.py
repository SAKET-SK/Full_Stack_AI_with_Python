# Authentication Decorator Example
# This decorator checks if a user is authenticated before allowing access to the function.
from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied. Admins only.")
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_sensitive_data(user_role):
    print("Accessing sensitive data...")

# Test cases
access_sensitive_data("guest")  # Should print "Access Denied. Admins only."
access_sensitive_data("admin")  # Should print "Accessing sensitive data..."
