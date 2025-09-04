# Suppose you run a cake shop and few flavors are discontinued. You want to skip.
# TO DO: Skip <Continue> if the flavor is "Out of Stock" ; Break <Break> if the flavor is "Discontinued"

flavors = ["Chocolate", "Vanilla", "Strawberry", "Out of Stock", "Mango", "Discontinued", "Butterscotch"]

for flavor in flavors:
    if flavor == "Out of Stock":
        continue  # Skip this flavor and move to the next iteration
    if flavor == "Discontinued":
        break  # Stop the loop entirely
    print(f"Available flavors: {flavor}")

print("End of the flavor list.")

