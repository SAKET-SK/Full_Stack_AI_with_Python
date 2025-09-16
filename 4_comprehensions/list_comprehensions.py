# Comprehensions in Python provide a concise way to create lists, sets, or dictionaries.
# They are shorter and often more readable than traditional loops.

# List comprehensions are particularly popular for their readability and efficiency.

things = ["Salted Chips", "Socks", "Tomatoes", "Salted Banana Chips", "Washing Powder"]

# Syntax: [expression for item in iterable if condition]
# Parts:
# 1. expression: The value to be added to the new list.
# 2. for item in iterable: The loop that goes through each item in the iterable.
# 3. if condition: (Optional) A filter that only includes items that meet the condition.
# Execution order: for -> if -> expression

salted_things = [item for item in things if "Salted" in item]  # List comprehension to filter items containing "Salted"
print(salted_things)  # Output: ['Salted Chips', 'Salted Banana Chips']

small_things = [small_item for small_item in things if len(small_item) < 10]  # Filter items with length less than 10
print(small_things)  # Output: ['Socks', 'Tomatoes']

