# Complex Try
# This code demonstrates the use of try, except, else, and finally blocks in Python.

def pack_office_bag(item):
    try:
        print(f"Packing {item} into the office bag.")
        if item == "unknown" or item == "explosives" or item == "weapons" or item == "drugs":
            raise ValueError("Item is unknown and can be dangerous; cannot be packed.")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"{item} packed successfully!")
    finally:                  # This block will always execute. Very useful for cleanup actions.
        print("Finished attempting to pack the item.\nTime to pack the next one.\n")
        print("---")

# Testing the function with different items
pack_office_bag("Laptop")
pack_office_bag("unknown")
pack_office_bag("explosives")
pack_office_bag("Notebook")
pack_office_bag("Pen")
pack_office_bag("weapons")  
pack_office_bag("drugs")
pack_office_bag("Water Bottle")
