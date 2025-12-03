# Thread Example 1 : Basic Threading Operations

import threading
import time

def read_paper():
    print(f"Started Reading Newspaper...")
    time.sleep(2)
    print(f"Finished Reading Newspaper...")

def read_magazine():
    print(f"Started Reading Magazine...")
    time.sleep(4)
    print(f"Finished Reading Magazine...")

start = time.time()
t1 = threading.Thread(target=read_paper)
t2 = threading.Thread(target=read_magazine)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Total Execution Time : {end - start:.2f} seconds")   # Total Execution Time : 4.00 seconds