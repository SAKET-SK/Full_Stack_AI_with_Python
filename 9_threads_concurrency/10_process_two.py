# Improvising on the previous code

from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Started CPU Intensive Task...")
    total = 0
    for i in range(10**7):
        total += i
    print(f"Completed CPU Intensive Task...")

if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(3)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    end = time.time()
    print(f"Total Execution Time : {end - start:.2f} seconds")     # otal Execution Time : 0.98 seconds

# Try increasing the number (10**7) to 8 and 9, will take approx 3.08 and 30.45 seconds respectively.
# If we increased the same number in previous code file, it crashed, took very very long.
