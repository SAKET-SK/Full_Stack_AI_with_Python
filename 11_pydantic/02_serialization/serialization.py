# Serialization in Pydantic
# It means converting a Pydantic model instance into a different format, such as JSON or a dictionary, and other formats.

from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime     # This can be a problem, as datetime is not directly serializable
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y  %H:%M:%S')  # Custom encoder for datetime
        }
    )

user = User(
    id=1,
    name="John Doe",
    email="johndoe@email.com",
    is_active=False,
    created_at=datetime(2024, 6, 1, 12, 14, 30),  # Year, Month, Day, Hour, Minute, Second, Microsecond
    address=Address(
        street="123 Main St",
        city="Anytown",
        zip_code="12345"
    ),
    tags=["admin", "user"]
)

# Serialize to dictionary
user_dict = user.model_dump()    # This converts the model to a dictionary

# Print the serialized outputs
print("As Pydantic Model Instance:")
print(user)

print("="*50)

print("As Dictionary:")
print(user_dict)

json_data = user.model_dump_json()  # This converts the model to a JSON string
print("="*50)

print("As JSON String:")
print(json_data)
