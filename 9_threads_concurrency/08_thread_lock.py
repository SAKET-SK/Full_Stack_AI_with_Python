# Using locks for shared state

import threading

counter = 0
lock = threading.Lock()    # Create a lock object

def increment_counter():
    global counter
    for _ in range(10000):
        with lock:
            counter += 1      # This locks that part of memory location for you

# This is a thread safe method

threads = [threading.Thread(target=increment_counter) for _ in range(10)]    # Comprehension for creating 10 threads
[t.start() for t in threads]
[t.join() for t in threads]
print(counter)