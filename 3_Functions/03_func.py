# Hiding implementation details with functions
# Functions allow us to hide complex implementation details behind a simple interface.
# Users of the function do not need to understand how it works internally; they just need to know how to use it.

# PROBLEM STATEMENT: You want to manage guest check-ins and check-outs efficiently.
# TO DO: Write functions to check in a guest, display guest information, etc.
# When a function called check_in is called, it should call 3 other functions:
# 1. Get guest's name and room number as input.
# 2. Validate the room number (it should be a positive integer).
# 3. Save to the db (for simplicity, just print a message with details of name and room number).

def get_guest_info():  # Function to get guest's name and room number
    print("Getting guest information...")

def validate_room_number():  # Function to validate room number
    print("Validating room number...")

def save_to_db():  # Function to save guest info to the database
    print("Saving guest information to the database...")

def check_in():  # Main function to check in a guest
    print("Starting check-in process...")
    get_guest_info()
    validate_room_number()
    save_to_db()
    print("Check-in process completed.")

check_in()  # Calling the main function to check in a guest

