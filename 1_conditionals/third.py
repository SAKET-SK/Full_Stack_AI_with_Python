# A tea stall offers different prizes based on the type of tea ordered.
# The tea stall has the following teas available:
# - Green Tea (costs $3)
# - Black Tea (costs $2)
# - Herbal Tea (costs $4)
# You are to take the input, if the tea is Green Tea, print "The cost is $3".
# If the tea is Black Tea, print "The cost is $2".
# If the tea is Herbal Tea, print "The cost is $4".
# If the tea is not available, print "Sorry, we don't have that tea."

input_tea = input("Which tea would you like to order? (Green Tea / Black Tea / Herbal Tea) ").lower()

if input_tea == "green tea":
    print(f"The cost of {input_tea} is $3")
elif input_tea == "black tea":
    print(f"The cost of {input_tea} is $2")
elif input_tea == "herbal tea":
    print(f"The cost of {input_tea} is $4")
else:
    print(f"Sorry, we don't have {input_tea}.")
