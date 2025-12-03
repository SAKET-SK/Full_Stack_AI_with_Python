from multiprocessing import Process, Value

def increment_counter(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1

if __name__ == '__main__':
    counter = Value('i',0)     # This takes the values in key-value format. This Value thing automatically gets its lock
    processes =[Process(target=increment_counter, args=(counter,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(counter.value)     # .value is basically a 'value' in ('i',0) i.e. in this example, 0