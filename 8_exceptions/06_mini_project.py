# Mini Project: A bill generator with exception handling

class InvalidItemError(Exception): pass

def generate_bill(item, price):
    menu = {"Biscuits": 20, "Chips": 10, "Water Bottle": 30}
    try:
        if item not in menu:
            raise InvalidItemError(f"Item '{item}' is not available in the menu.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        total = menu[item] * price
        print(f"The total bill for your order is : {total} bucks.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for visiting our shop!")

# Testing the bill generator with different scenarios
generate_bill("Biscuits", 2)        # Valid case
generate_bill("Chocolate", 2)       # InvalidItemError case
generate_bill("Chips", "five")     # TypeError case


