# Thread Example 2 : Passing Arguments to Threads

import threading
import time

def read_something(type_, readTime):
    print(f"Started reading {type_} page from newspaper...")
    time.sleep(readTime)
    print(f"Finished reading {type_} page from newspaper...")

t1 = threading.Thread(target=read_something, args=("sports", 2))
t2 = threading.Thread(target=read_something, args=("fashion", 3))
t3 = threading.Thread(target=read_something, args=("politics", 6))

# Important point : How are we passing the arguments to the threads?
# These are in the form of tuples, and you can send as many as you want, just refer the method signature

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()