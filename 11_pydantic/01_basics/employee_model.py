# Adding validators using Field

from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,        # ... indicates that this field is required   
        min_length=2, 
        max_length=50,
        description="The full name of the employee",
        examples="John Doe"
    ) 
    department: Optional[str] = 'General'  # Optional field with a default value
    salary: float = Field(
        ...,
        ge=10000,    # Greater than or equal to 10000
        # similartly, you can use le (less than or equal to), gt (greater than), lt (less than)
    )