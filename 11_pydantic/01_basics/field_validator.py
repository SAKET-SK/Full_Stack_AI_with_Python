# Field and Model Validators in Pydantic

from pydantic import BaseModel, field_validator, model_validator

# Using field_validator to add custom validation logic
class User(BaseModel):
    username: str

    @field_validator('username')    # This is a decorator for field validation   
    def username_length(cls, v):    # cls refers to the class; whole class is available to it, v is the value being validated
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters long')
        return v
    
# Field validators are for a specific field only
# However, Model validators can validate across multiple fields

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')   # This is a decorator for model-level validation
    def passwords_match(cls, values): # values is a dict of all field values
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values