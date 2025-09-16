# Set Comprehensions in Python provide a concise way to create sets.
# They are shorter and often more readable than traditional loops.
# Set comprehensions are similar to list comprehensions but use curly braces {} instead of square brackets [].
# Sets automatically handle duplicate values, so any duplicates in the input will be removed in the output set.

things_in_basket = ["Salted Chips", "Socks", "Tomatoes", "Salted Banana Chips", "Washing Powder", "Socks", "Tomatoes"]

# Syntax: {expression for item in iterable if condition}
# Parts:
# 1. expression: The value to be added to the new set.
# 2. for item in iterable: The loop that goes through each item in the iterable.
# 3. if condition: (Optional) A filter that only includes items that meet the condition.
# Execution order: for -> if -> expression

unique_things = {item for item in things_in_basket}  # Set comprehension to create a set of unique items
print(unique_things)  # Output: {'Salted Chips', 'Socks', 'Tomatoes', 'Salted Banana Chips', 'Washing Powder'}
# Note: The order of items in a set is not guaranteed.
# Also you may have noticed we have skipped the if condition here. It's optional.

town_parts = {
    "North": ["Temple", "Market", "Library", "Gym"],
    "South": ["Park", "Museum", "Cafe"],
    "East": ["School", "Hospital", "Park", "Cafe"],
    "West": ["Beach", "Harbor", "Theater"],
    "Central": ["Mall", "City Hall", "Stadium", "Library"]
}

unique_buildings = {building for buildings in town_parts.values() for building in buildings}
# Explaination:
# 1. town_parts.values() gives us the lists of buildings in each part of the town.
# 2. The outer loop (for buildings in town_parts.values()) iterates over each list of buildings.
# 3. The inner loop (for building in buildings) iterates over each building in the current list.
# 4. The expression (building) adds each building to the set, automatically handling duplicates.

print(unique_buildings)  # Output: {'Temple', 'Market', 'Library', 'Gym', 'Park', 'Museum', 'Cafe', 'School', 'Hospital', 'Beach', 'Harbor', 'Theater', 'Mall', 'City Hall', 'Stadium'}
