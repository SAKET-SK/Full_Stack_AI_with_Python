from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

# Example 1 : Multiple Field Validators
class User(BaseModel):
    first_name: str
    last_name: str

    # Multiple field validators for first_name and last_name
    @field_validator('first_name', 'last_name')
    def check_name_capitalization(cls, v):
        if not v.istitle():
            raise ValueError('Names must be capitalized')
        return v
    
# Example 2 : Data Transformation Patterns
class Person(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, v):
        return v.lower().strip()     # strip whitespace and convert to lowercase
    
# Example 3 : You may also run the validation before the model

class Product(BaseModel):
    price: str   # We will convert this to float later, example value: "$1,234"

    @field_validator('price', mode='before')
    def convert_price_to_float(cls, v):
        if isinstance(v, str):
            # return float(v.replace('$', '').replace(',', ''))   # Replace $ and , before conversion with nothing
            return float(v.replace('$', ''))
        return v
    
# Example 4 : Going more complex with datetime parsing

class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError('start_date must be before end_date')
        return values
