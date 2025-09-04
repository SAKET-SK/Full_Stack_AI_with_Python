# Problem Statement
# A cafe owner has a digital token to display, for every customer in line, the number is printed and customer is served his/her order.

# TO DO : use for loop to generate token numbers from 1 to 10, use range()
# Also keep printing after each iteration "Customer number i, please collect your order"

for token_number in range(1, 11):      # Loop from 1 to 10; 11 is non-inclusive
    print(f"Customer #{token_number}, please collect your order")

# Let's have another example
# This cafe prepares orders in batch every 10 minutes; simulate 4 batches

# TO DO : use range() to simulate batch numbers; and keep informing "Batch number i is ready"

for batch in range(1, 5):
    print(f"Batch number {batch} is ready.")
