# Generator comprehension
# Generator comprehensions in Python provide a concise way to create generators.
# They are similar to list comprehensions but use parentheses () instead of square brackets [].
# Generators are more memory efficient than lists because they generate items on-the-fly and do not store them in memory.
# This makes them suitable for working with large datasets or streams of data.

# Syntax: (expression for item in iterable if condition)
# Parts:
# 1. expression: The value to be yielded by the generator.
# 2. for item in iterable: The loop that goes through each item in the iterable.
# 3. if condition: (Optional) A filter that only includes items that meet the
# Execution order: for -> if -> expression

money_in_each_room = [100, 200, 150, 300, 250]

total_money = sum(money for money in money_in_each_room)  # Generator comprehension to sum money in each room
print(total_money)  # Output: 1000
