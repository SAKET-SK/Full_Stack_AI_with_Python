import threading
import time

def cpu_heavy():
    print(f"Started CPU Intensive Task...")
    total = 0
    for i in range(10**7):
        total += i
    print(f"Completed CPU Intensive Task...")

start = time.time()
threads = [threading.Thread(target=cpu_heavy) for _ in range(3)]
[t.start() for t in threads]
[t.join() for t in threads]
end = time.time()
print(f"Total Execution Time : {end - start:.2f} seconds")   # Total Execution Time : 1.33 seconds

# But this is not an efficient way. Can we do the same process a bit more faster?
# We will see in another code file.