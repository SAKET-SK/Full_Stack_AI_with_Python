ice_cream_flavors = ("vanilla", "chocolate", "strawberry") # A sample tuple -> immutable ordered collection

(flavor1, flavor2, flavor3) = ice_cream_flavors # Tuple unpacking - assigning each value to a variable
print(f"Flavor 1 is {flavor1}, Flavor 2 is {flavor2}, Flavor 3 is {flavor3}")
# Tuples are immutable

milk_ratio, sugar_ratio = 4, 3
print(f"Milk ratio is {milk_ratio}, Sugar ratio is {sugar_ratio}")
milk_ratio, sugar_ratio = sugar_ratio, milk_ratio # Swapping values 
print(f"After swapping - Milk ratio is {milk_ratio}, Sugar ratio is {sugar_ratio}")
# variable swapping does not need a temp / third variable in Python

# Membership test
print(f"Is chocolate flavor available? {'chocolate' in ice_cream_flavors}")  # True -> But be careful with case sensitivity!!
print(f"Is chocolate flavor available? {'Chocolate' in ice_cream_flavors}")  # False -> Case sensitive issue
print(f"Is mango flavor available? {'mango' in ice_cream_flavors}")          # False -> Not available
