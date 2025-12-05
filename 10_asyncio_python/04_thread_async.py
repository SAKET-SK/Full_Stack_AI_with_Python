# Can Async and Multithreading work together? 
# Answer: Yes, you will understand it better when you see the code

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor   # executes all threads in a pool; this is basically asyncio.gather, but for the threads

def check_stock(item):
    print(f"Checking stock for {item} ...")
    time.sleep(3)        # Blocking Operation
    return f"{item} is in stock!"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Laptop")  # This allows you to run async function but in another thread as main thread is blocked.
        # This spins up a whole new thread and does its work there
        print(result)

asyncio.run(main())