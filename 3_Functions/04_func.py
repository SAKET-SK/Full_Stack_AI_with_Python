# Improving readability with functions
# Functions enhance code readability by providing meaningful names to code blocks.
# A well-named function can convey its purpose, making the code easier to understand at a glance.
# This is especially useful in larger codebases where understanding the flow of logic is crucial.

# PROBLEM STATEMENT: Your building has different kinds of rooms: single, double, suite.
# Instead of writing formulas everywhere, create a function.

# TO DO: write calculate_price(room_type, nights), return the total price. Use this function for multiple room types and nights.

def calculate_price(room_type, nights):  # Function to calculate price based on room type and number of nights
    if room_type == "single":
        price_per_night = 100
    elif room_type == "double":
        price_per_night = 150
    elif room_type == "suite":
        price_per_night = 300
    else:
        return "Invalid room type"
    
    return price_per_night * nights
    

# Using the function for different room types and nights

total_price = calculate_price("double", 3)
print(f"Total price for 3 nights in a double room: ${total_price}")
total_price = calculate_price("suite", 2)
print(f"Total price for 2 nights in a suite: ${total_price}")
total_price = calculate_price("single", 5)
print(f"Total price for 5 nights in a single room: ${total_price}")
total_price = calculate_price("deluxe", 4)
print(f"Total price for 4 nights in a deluxe room: {total_price}")
