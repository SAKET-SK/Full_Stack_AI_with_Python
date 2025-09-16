# Dictionary Comprehension allows you to create dictionaries in a concise way.
# They are similar to list comprehensions but use curly braces {} and key-value pairs.
# Dictionary comprehensions can also include conditions to filter items.
# They are often more readable and efficient than traditional loops for creating dictionaries.

# Syntax: {key_expression: value_expression for item in iterable if condition}

item_prices = {
    "Salted Chips": 2.5,
    "Socks": 5.0,
    "Tomatoes": 3.0,
    "Salted Banana Chips": 2.0,
    "Washing Powder": 10.0
}

# Lets convert prices from dollars to euros (assuming 1 dollar = 0.85 euros)

euro_prices = {item: price * 0.85 for item, price in item_prices.items()}
print(euro_prices)

# This will output: the converted prices in euros
