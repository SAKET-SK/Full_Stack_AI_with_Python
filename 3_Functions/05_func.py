# Improving Traceability with Functions
# Functions can help improve traceability by isolating specific tasks or operations.
# When an issue arises, you can trace it back to a specific function rather than sifting through a large block of code.
# This makes debugging and maintenance easier.

# PROBLEM STATEMENT: You tend to add 15% room living tax on stay bills. You want this to be consistent and traceable.
# TO DO: Write add_tax(price, tax_rate). Use it to compute final prices for 3 orders.

def add_tax(price, tax_rate):  # Function to add tax to a given price
    return price * (100 + tax_rate) / 100  # Simplified calculation

recent_orders = [100, 250, 400]  # List of recent order prices

for order in recent_orders:
    final_price = add_tax(order, 15)  # Calling the function to add tax
    print(f"Final price after tax for order {order} is: ${final_price:.2f}")  # Formatted output

# Traceability is improved because if there's an issue with tax calculation, we only need to check the add_tax function.
