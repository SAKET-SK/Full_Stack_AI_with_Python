# Race condition in Python

# A Race condition occurs when multiple threads or processes access shared data and try to change it at the same time.
# Because the thread scheduling algorithm can swap between threads at any time, you don't know the order in which the threads will attempt to access the shared data.

import threading

value = 0

def change_value():
    global value
    for _ in range(100000):
        value += 1

threads = [threading.Thread(target=change_value) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print(f"Final value: {value}")  # The final value

# Race condiion may occur when two threads try to update the value variable at the same time.
# This code is unpredictble as it has no locking mechanism, no idea which thread is operting on the value variable at a given time.
# You may also see final value as 200000 sometimes, but most of the times it will be less than that.