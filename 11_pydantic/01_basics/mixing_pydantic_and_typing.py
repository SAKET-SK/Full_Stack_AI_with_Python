# Mixing Pydantic with typing module

from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]         # You can use List from typing, inside of it, the items will be of type str
    quantities: Dict[str, int]  # A dictionary with string keys and integer values

class Blogpost(BaseModel):
    title: str
    content: str
    image: Optional[str] = None  # Optional field, can be None. This field can be string or it can be None.

cart_data = {
    'user_id': 123,
    'items': ['Laptop', 'Mouse', 'Keyboard'],
    'quantities': {'Laptop': 1, 'Mouse': 2, 'Keyboard': 1}
}

cart = Cart(**cart_data)
print(cart)