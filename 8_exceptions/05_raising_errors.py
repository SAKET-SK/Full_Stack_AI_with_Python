# Raising your own errors / custom exceptions in Python
# In Python, you can raise your own exceptions using the 'raise' statement.

def check_office_item(item):
    if item not in ["Laptop", "Water Bottle", "Notebook", "Pen"]:
        raise ValueError(f"The item '{item}' is not a valid office essential.")
    print(f"Packing {item} into the office bag.")

check_office_item("Laptop")  # Valid item
check_office_item("Tablet")  # This will raise a ValueError

# Comment the above code to allow the next part to run without interruption, because of ValueError, it will not be executed.

# You can also create custom exception classes by inheriting from the built-in Exception class.
class OfficeItemError(Exception):
    """Custom exception for invalid office items."""
    pass

def pack_office_item(item):
    if item not in ["Laptop", "Water Bottle", "Notebook", "Pen"]:
        raise OfficeItemError(f"The item '{item}' cannot be packed as it is not an office essential.")
    print(f"{item} packed successfully!")

pack_office_item("Notebook")  # Valid item
pack_office_item("Joker Costume")  # This will raise an OfficeItemError