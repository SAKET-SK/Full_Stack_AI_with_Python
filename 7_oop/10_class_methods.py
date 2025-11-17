# Class Methods Example
# Class methods are methods that are bound to the class and not the instance of the class.
# They can access and modify class state that applies across all instances of the class.

class Cafe_Orders:
    def __init__(self, order_id, no_of_items, type_of_order):
        self.order_id = order_id
        self.no_of_items = no_of_items
        self.type_of_order = type_of_order

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data['order_id'],
            order_data['no_of_items'],
            order_data['type_of_order']
        )    
    # Its like calling a constructor from the same class.
    # Behind the scene, it is the same constructor as above which is being called here.

    @classmethod
    def from_string(cls, order_string):
        order_id, no_of_items, type_of_order = order_string.split("-")
        return cls(order_id, int(no_of_items), type_of_order)
    
order1 = Cafe_Orders.from_dict({'order_id': '001', 'no_of_items': 3, 'type_of_order': 'Dine-In'})
order2 = Cafe_Orders.from_string("002-5-Takeaway")
order3 = Cafe_Orders("003", 2, "Dine-In")

print(order1)   # <__main__.Cafe_Orders object at 0x000001CB6D444B50>
print(order1.__dict__)  # {'order_id': '001', 'no_of_items': 3, 'type_of_order': 'Dine-In'}
print(order2)   # <__main__.Cafe_Orders object at 0x000001CB6D444BD0>
print(order2.__dict__)  # {'order_id': '002', 'no_of_items': 5, 'type_of_order': 'Takeaway'}

# No object is created for class methods.
# They are called using the class name itself.