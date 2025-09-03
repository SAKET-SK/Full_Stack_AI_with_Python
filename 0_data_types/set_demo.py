rich_dude_1 = {"Car", "Riverside Resort", "Yacht"}
rich_dude_2 = {"Yacht", "Private Jet", "Mansion", "Car"}

items_owned_by_rich = rich_dude_1 | rich_dude_2  # Union of two sets - all unique items
print(f"All items owned by both rich dudes: {items_owned_by_rich}")

common_items = rich_dude_1 & rich_dude_2  # Intersection of two sets - common items
print(f"Common items owned by both rich dudes: {common_items}")

unique_to_rich_dude_1 = rich_dude_1 - rich_dude_2  # Difference - items only owned by rich_dude_1
print(f"Items only owned by rich dude 1: {unique_to_rich_dude_1}")

# Membership test
print(f"Does rich dude 1 own a Yacht? {'Yacht' in rich_dude_1}")  # True
print(f"Does rich dude 2 own a Riverside Resort? {'Riverside Resort' in rich_dude_2}")  # False
