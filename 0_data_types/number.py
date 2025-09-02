money = 12000
print(f"Your salary during stipend is {money}")

money = 25000
print(f"Your salary after stipend is {money}")

# But can we say number is mutable? No, numbers are immutable

# Let's check the id of the number
print(f"ID of 12000 is {id(12000)}")
print(f"ID of 25000 is {id(25000)}")

# OUTPUT:
# Your salary during stipend is 12000
# Your salary after stipend is 25000
# ID of 12000 is 3059587587376
# ID of 25000 is 3059587595408

# Never come to the conclusion that numbers are mutable just because the variable name is same. Always check its ID
# If the ID changes, it means a new object is created in memory. We just chnaged the reference. Hence numbers are immutable

# If the ID remains same, it means the same object is being referenced. Hence immutable
