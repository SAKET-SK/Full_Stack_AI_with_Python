# Threading in Python allows for concurrent execution of code, enabling multiple threads to run simultaneously within a single process. This is particularly useful for I/O-bound tasks where threads can wait for external resources without blocking the entire program.

# Particularly, threading is beneficial in scenarios such as:
# 1. I/O-bound operations: Tasks that involve waiting for external resources, such as file I/O, network requests, or database queries.
# 2. User interfaces: Keeping the UI responsive by offloading long-running tasks to separate threads.
# 3. Background tasks: Running periodic tasks or background services without interrupting the main application flow.

import threading
import time

start_time = time.time()
def pack_bag():
    for i in range(1, 4):
        print(f"Packing item {i}")
        time.sleep(1)  # Simulate time taken to pack an item

def book_flight():
    for i in range(1, 4):
        print(f"Booking flight step {i}")
        time.sleep(2)  # Simulate time taken to book a flight

# Create threads for packing bag and booking flight
pack_thread = threading.Thread(target=pack_bag)
flight_thread = threading.Thread(target=book_flight)

# Start the threads
pack_thread.start()
flight_thread.start()

# Wait for both threads to complete
# Behind the scenes, join() means that after you finish, report back to me.
pack_thread.join()
flight_thread.join()

end_time = time.time()
print("All tasks completed. Ready for the trip!")
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")     # 6.0036 seconds

# Note: The execution time may vary slightly with each run due to the nature of threading and system load.
