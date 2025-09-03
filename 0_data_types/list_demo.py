name_list = ["Saket", "Rohan", "Sagar", "Sharad"]

# Lists are mutable, if it were a tuple, we cannot add new values in case we forgot
name_list.append("Soumyadeep")  # Adding a new name to the list, at the end
print(f"OG People in my team: {name_list}")
name_list.remove("Sharad")      # Removing a name from the list
print(f"People in my team after removing one recruit: {name_list}")

other_team = ["Amol", "Vishal"]
name_list.extend(other_team)      # Merging two lists
print(f"People in my team after including other team: {name_list}")

name_list.insert(2, "Sharad")  # Inserting a name at a specific index
print(f"People in my team after adding someone at specific place: {name_list}")

latest_person = name_list.pop()  # Removing the last person from the list and returning the value
print(f"Latest person who left the team: {latest_person}")
print(f"People in my team: {name_list}")

name_list.reverse()  # Reversing the list
print(f"Reversed list of people in my team: {name_list}")

name_list.sort()     # Sorting the list in ascending order
print(f"Sorted list of people in my team: {name_list}")

salary_list = [50000, 60000, 55000, 70000, 65000]
print(f"Maximum salary in the team: {max(salary_list)}")
print(f"Minimum salary in the team: {min(salary_list)}")

# Operator Overloading
list1 = [1, 2, 3]
list2 = [4, 5, 6]   
print(f"Concatenated List: {list1 + list2}")  # Concatenation
print(f"Repeated List: {list1 * 3}")           # Repetition

raw_items = bytearray(b"Rice") # A sample bytearray -> mutable ordered collection of bytes
print(f"Raw items before modification: {raw_items}")
new_raw_items = raw_items.replace(b"Rice", b"Rye") # Modifying bytearray
print(f"Raw items after modification: {new_raw_items}")
