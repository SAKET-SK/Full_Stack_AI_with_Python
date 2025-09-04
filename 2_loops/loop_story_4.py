# There are 2 lists. One contains the item name and the other contains the price of the item.
# Print the item name along with its price : '[item] - $[price]'

items = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
prices = [50, 30, 70, 20, 150]

for item_name, item_price in zip(items, prices):
    print(f"{item_name} - ${item_price}")
