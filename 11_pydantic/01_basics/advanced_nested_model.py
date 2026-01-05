# Advanced Nested Model Example with Pydantic

from typing import List, Optional, Union
from pydantic import BaseModel

# Example 1 : Optional Nested Model
class Address(BaseModel):
    city: str
    street: str
    zip_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None  # Company may or may not have an address; they might be remote

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None  # Employee may or may not be associated with a company

# Example 2 : Mixed Data Types in Nested Models

class TextContent(BaseModel):
    type: str = "text"
    blog_content: str

class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str

class BlogPost(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]  # sections can be either TextContent or ImageContent

# Example 3 : Deeply Nested Structures

class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Resident(BaseModel):
    name: str
    city: City
    street: str