# Building a ticket info system for a railway app.
# Input : sleeper, AC, general, luxury
# Match using : match-case
# Output : "You have selected a [class] ticket. Enjoy your journey!" If invald class, print "Invalid ticket class selected."

seat_type = input("Enter the type of ticket you want (sleeper, AC, general, luxury): ").lower()

match seat_type:
    case "sleeper":
        print(f"You have selected a {seat_type} ticket. Enjoy your journey!")
    case "ac":
        print(f"You have selected an {seat_type} ticket. Enjoy your journey!")
    case "general":
        print(f"You have selected a {seat_type} ticket. Enjoy your journey!")
    case "luxury":
        print(f"You have selected a {seat_type} ticket. Enjoy your journey!")
    case _:
        print("Invalid ticket class selected.")

# Expected output: "You have selected a [class] ticket. Enjoy your journey!" (if valid class)
# If invald class, print "Invalid ticket class selected."
