# Nothing to do with Loops, just to demonstrate the walrus operator.
# The walrus operator (:=) allows you to assign values to variables as part of an expression.
# This can be particularly useful in situations where you want to both assign a value and use it in a condition or loop.

# Recently added in Python 3.8, the walrus operator can help make your code more concise and readable by reducing redundancy.

# Example without walrus operator
value = 17
remainder = value % 3

if remainder:
    print(f"{value} is not divisible by 3, remainder is {remainder}")

# Example with walrus operator

if (remainder := value % 3):
    print(f"{value} is not divisible by 3, remainder is {remainder}")

# Another example: Input validation

available_items = ["apple", "banana", "orange"]
if(requested_item := input("Which fruit do you want? ").lower()) in available_items:
    print(f"Here is your {requested_item}.")
else:
    print(f"Sorry, we don't have {requested_item}.")

# Another example: using walrus operator in a while loop
# This loop will keep asking for user input until the user inputs valid flavor
valid_flavors = ["chocolate", "vanilla", "strawberry"]
print(f"Available flavors: {valid_flavors}")

while (flavor := input("Choose a flavor: ").lower()) not in valid_flavors:
    print(f"Sorry, {flavor} is not available. Please choose again.")

print(f"Great choice! Here is your {flavor}.")
