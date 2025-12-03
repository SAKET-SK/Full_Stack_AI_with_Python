# Common issue : In any of the processes, communication is a bit of a challenge. Memory is not shared
# between processes, and you need to pass data from one process to another.
# To pass data between processes, you can use queues or pipes.

# Queue : A queue is a data structure that is used to store data in a first-in-first-out (FIFO) manner.
# It is a simple data structure that is used to store data in a linear manner.

from multiprocessing import Process, Queue
import time

def pack_bag(queue):
    queue.put('camera')     # You may put anything in here, dictionary, list, etc.

if __name__ == "__main__":
    queue = Queue()

    p = Process(target=pack_bag, args=(queue,))
    p.start()
    p.join()
    print(queue.get())

# Significance : Now Queue is like a another data structure.
# The same thing will be passed to as many as process as you want