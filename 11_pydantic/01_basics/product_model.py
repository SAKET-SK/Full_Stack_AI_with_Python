# Foundations of Pydantic: Defining a Model

from pydantic import BaseModel

class Product(BaseModel):
    product_id: int
    name: str
    price: float
    in_stock: bool = True  # Default value set to True

product_1 = Product(product_id=101, name="Smartphone", price=699.99, in_stock=True)
product_2 = Product(product_id=102, name="Headphones", price=199.99)  # in_stock will default to True
# product_3 = Product(name="Tablet", price=299.99 in_stock=True)  # This will raise an error due to missing product_id