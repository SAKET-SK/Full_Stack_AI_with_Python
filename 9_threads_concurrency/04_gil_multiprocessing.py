# GIL using Multiprocessing in Python
# The Global Interpreter Lock (GIL) in Python can be a limitation for CPU-bound tasks
# when using threading, as it allows only one thread to execute Python bytecode at a time
# within a single process. To bypass the GIL and achieve true parallelism, the multiprocessing
# module can be used. This module creates separate processes, each with its own Python interpreter  
# and memory space, allowing multiple CPU-bound tasks to run simultaneously.

from multiprocessing import Process
import time

def change_money():
    print(f"{time.ctime()}: Starting to change money.")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{time.ctime()}: Finished changing money.")

if __name__ == "__main__":
    start = time.time()
    process1 = Process(target=change_money)
    process2 = Process(target=change_money)
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.time()

    print(f"Total execution time with multiprocessing: {end - start:.4f} seconds")  # 4.7430 seconds


