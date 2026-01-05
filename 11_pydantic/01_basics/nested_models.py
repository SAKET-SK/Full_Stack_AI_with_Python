# Nested models in Pydantic
# We can use one Pydantic model as a field in another Pydantic model.

from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    name: str
    address: Address  # Nested model; the type is another Pydantic model, defined up above

# Model Composition 
# The "User" contains an "Address" model as one of its fields. Baically it contains the reference of Address model.
# Also notice type annotation of address field is Address model.

home_address = Address(
    street="123 Main St",
    city="Springfield",
    state="IL",
    zip_code="62701"
)

user_details = User(
    name="John Doe",
    address=home_address
)

# Alternative approach via dictionary
also_user_details = {
    "name": "John Doe",
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62701"
    }
}

user = User(**also_user_details)  # Unpacking dictionary to create User instance; never forget the ** while passing the dictionary
print(user)