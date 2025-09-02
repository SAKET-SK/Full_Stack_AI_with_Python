munchies = set()
print(f"Initial ID of munchies is {id(munchies)}")
munchies.add("Pizza")
munchies.add("Burger")
munchies.add("Pasta")
print(munchies)
print(f"Final ID of munchies is {id(munchies)}")

# OUTPUT:
# Initial ID of munchies is 2746118299360
# {'Pizza', 'Pasta', 'Burger'}
# Final ID of munchies is 2746118299360

# Sets are mutable as the ID remains same even after adding elements to it
