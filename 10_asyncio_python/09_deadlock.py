# Deadlock in Python

# A Deadlock occurs when two or more threads are blocked forever, each waiting for the other to release a resource.
# Deadlocks can occur when multiple threads need the same locks but obtain them in a different order.

import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
    with lock_a:
        print("Task 1 acquired lock A")
        with lock_b:
            print("Task 1 acquired lock B")

def task2():
    with lock_b:
        print("Task 2 acquired lock B")
        with lock_a:
            print("Task 2 acquired lock A")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

# Task 2 will keep on waiting for lock A, which is held by Task 1.
# That menans our code will hang here forever.
# Classic deadlock situation.