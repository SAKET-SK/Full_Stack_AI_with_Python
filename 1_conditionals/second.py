# A snack suggestor
# A local cafe wants a python program that suggests a snack based on its availability.
# The cafe has the following snacks available:
# - Cookies (available)
# - Brownies (not available)
# - Muffins (available)
# - Donuts (not available)
# You are to take the input, if the snack is Cookies or Muffins, print "Snack is available!". Else, print "Snack is not available."

snack = input("What would you like to eat? ").lower()

print(f"User has ordered: {snack}")

if snack == "cookies" or snack == "muffins":
    print(f"We will prepare {snack} for you shortly. Snack is available!")
else:
    print("Snack is not available. We only serve Cookies and Muffins.")
