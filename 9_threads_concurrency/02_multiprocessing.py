# Multi Processing Example in Python
# Multiprocessing in Python allows for the creation of separate processes that can run concurrently, each with
# its own Python interpreter and memory space. This is particularly useful for CPU-bound tasks that require
# significant computational power, as it can bypass the Global Interpreter Lock (GIL) and fully utilize multiple CPU cores.

from multiprocessing import Process
import time

start_time = time.time()
def take_medicine(name):
    print(f"Taking medicine: {name}")
    time.sleep(3)
    print(f"Finished taking medicine: {name}")

# What is happening here is that we are creating multiple processes to take medicine concurrently.
# Each process runs independently, allowing for parallel execution.
if __name__ == '__main__':
    medicine_takers = [
        Process(target=take_medicine, args=(f"Taking Medicine #{i+1}",))
        for i in range(3)
    ]

    for meds in medicine_takers:   # Start each process
        meds.start()

    for meds in medicine_takers:   # Wait for each process to complete
        meds.join()

    end_time = time.time()
    print("All medicines have been taken.")
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.4f} seconds")   # 3.2040 seconds
