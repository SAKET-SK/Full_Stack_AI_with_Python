# Splitting complex tasks using functions
# Functions help break down complex tasks into smaller, manageable parts.
# Each function can handle a specific part of the task, making the code easier to read and maintain.

# PROBLEM STATEMENT: You are keeping financial records for your guests.
# TO DO: Write functions to calculate the total bill, apply discounts, and generate a receipt.
# Example : calculate_total(bill_items), apply_discount(total, discount), generate_receipt(name, total); generate_report(guests) this should call all the other functions.

def calculate_total():  # Function to calculate total bill
    print("Calculating total bill...")

def apply_discount():  # Function to apply discount
    print("Applying discount...")

def generate_receipt():  # Function to generate receipt
    print("Generating receipt...")

def generate_report():  # Function to generate report for multiple guests
    print("Generating report for all guests...")
    calculate_total()  # Calling other functions
    apply_discount()
    generate_receipt()

# Calling the main function to generate report
generate_report()
