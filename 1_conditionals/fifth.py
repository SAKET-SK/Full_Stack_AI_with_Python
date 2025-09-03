# You run a restaurant. If someone orders online meal and the cost is more than $100, then delivery fee is waived.
# If the cost is less than $100, delivery fee is $10.

# Use ternary operator to decide the delivery fee and solve this problem.

order_cost = int(input("Enter the cost of online meal order: $")) 

delivery_fee = 0 if order_cost > 100 else 10

print(f"Delivery fee is: ${delivery_fee}")

