from pydantic import BaseModel     # Majority of the work will be done by BaseModel

# A Pydantic class must inherit from BaseModel
class Item(BaseModel):
    id: int
    name: str
    is_in_stock: bool

input_data = {'id': 1, 'name': "Laptop", 'is_in_stock': True}   # If you change any of these types, Pydantic will raise a validation error

item = Item(**input_data)  # Unpack the dictionary into the model; the ** operator is used for unpacking
print(item)
