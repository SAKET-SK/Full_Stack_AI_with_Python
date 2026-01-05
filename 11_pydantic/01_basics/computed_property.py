# Computed property example using Pydantic

from pydantic import BaseModel, computed_field, Field

class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field      # This decorator indicates that this is a computed property; it means it will be calculated upon access
    @property            # This makes it accessible like a regular attribute
    def area(self) -> float:       # The return type is specified as float
        return self.width * self.height
    
# An advanced example to boost confidence
class Hotel_Room_Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)  # Number of nights must be greater than or equal to 1; Also a mandatory field
    price_per_night: float

    @computed_field
    @property
    def total_price(self) -> float:
        return self.nights * self.price_per_night
    
booking = Hotel_Room_Booking(user_id=1, room_id=101, nights=3, price_per_night=150.0)
print(f"Total price for booking: ${booking.total_price}")  # Outputs: Total price for booking: $450.0

print(f"Model Dump: {booking.model_dump()}")  # Outputs the model data without the computed field

# Dump Output will be:
# {user_id: 1, room_id: 101, nights: 3, price_per_night: 150.0, total_price: 450.0}
# Haven't added total_price in dump as it's a computed field and has poperty decorator, it is visible there after calculation.
