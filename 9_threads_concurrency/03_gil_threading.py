# Global Interpreter Lock (GIL) in Python
# The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects,
# preventing multiple native threads from executing Python bytecodes at once. This means that
# even in a multi-threaded Python program, only one thread can execute Python code at a time.
# The GIL can be a bottleneck in CPU-bound and multi-threaded code, as it limits the performance
# improvements that can be achieved through threading.

import threading
import time

def do_task():
    print(f"{threading.current_thread().name} started to do a task.")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished the task.")

thread1 = threading.Thread(target=do_task, name="Thread-1")
thread2 = threading.Thread(target=do_task, name="Thread-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()   
print(f"Total execution time: {end - start:.4f} seconds")  # 7.2279 seconds

# Due to the GIL, the total execution time will be close to the time taken by
# a single thread to complete the task, rather than being halved as one might expect
# with true parallel execution.