# Sending data to a generator
# Generators can also receive data. This is done using the send() method.   
# The send() method resumes the generator and "sends" a value that becomes the result of the current yield expression.
# The first call to next() is still required to start the generator and advance it to the first yield expression.
# After that, send() can be used to send values to the generator.

def customer():
    print("Hello Customer! What would you like to order?")
    order = yield  # Yielding None initially, waiting for the first send() to provide an order
    while True:
        print(f"Preparing your {order}...")
        order = yield f"Here is your {order}. What would you like next?"  # Yielding the prepared order and waiting for the next order. Uncommenting this line will trigger an infinite loop. So it waits for the next send() call.

shop = customer()  # shop is a generator object; storing reference to the customer function
next(shop)  # Start the generator, advance to the first yield

shop.send("Pizza")  # Send first order

# Execution order:
# First, "Hello Customer! What would you like to order?" is printed when next(shop) is called. It stops there itself, expecting something via send().
# Then, "Preparing your Pizza..." is printed when shop.send("Pizza") is called.

shop.send("Burger")  # Send second order
shop.send("Pasta")   # Send third order
