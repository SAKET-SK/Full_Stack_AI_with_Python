# Static Methods in Python
# Static methods are methods that belong to a class rather than an instance of the class.
# They do not require access to instance (self) or class (cls) variables.

class Food_Plate:
    @staticmethod
    def hot_dish(text):
        return [item.strip() for item in text.split(",")]        # Splitting the text by comma to get individual food items.
        # Short hand for creating a list using for loop. 

raw = "  Pasta, Pizza, Salad , Burger  "

# Nothing wrong with this, this is the usual way of calling a method.
# But this is not the correct way to call a static method.
obj = Food_Plate()
obj.hot_dish(raw)

# Let me add annotation to indicate that this is a static method. Check Line Number 6.
# After adding @staticmethod annotation, we should call it using the class name.

hot_food = Food_Plate.hot_dish(raw)  # Correct way to call a static method.
print(hot_food)  # Output: ['Pasta', 'Pizza', 'Salad', 'Burger']