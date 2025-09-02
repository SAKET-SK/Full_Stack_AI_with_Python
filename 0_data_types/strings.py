food_order = "Chicken Cheese Burst Pizza"
customer_name = "Saket"
print(f"{customer_name}, your order for {food_order} is being prepared")

# Strings are immutable

# Indexing and Slicing

food_description = "Hot and freshly baked Chicken Cheese Burst Pizza"
print(f"First character of food description is {food_description[0:8:2]}")  # Htad -> Skipping every second character
print(f"First character of food description is {food_description[0:8]}")  # Hot and -> Slicing from index 0 to 7
print(f"First character of food description is {food_description[:8]}")  # Same as above
print(f"First character of food description is {food_description[0]}")  # H
print(f"Last character of food description is {food_description[16:]}")  # baked Chicken Cheese Burst Pizza
print(f"Reversed food description is {food_description[::-1]}")  # shortcut to reverse a string

label_text = "Markét"
encoded_label = label_text.encode("utf-8")  # Encoding string to bytes
print(f"Original label is {label_text}")
print(f"Encoded label is {encoded_label}")
decoded_label = encoded_label.decode("utf-8")  # Decoding bytes back to string
print(f"Decoded label is {decoded_label}")
