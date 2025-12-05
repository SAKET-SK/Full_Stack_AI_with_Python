# Asynchronous Programming in Python
# Asynchronous programming allows you to write code that can run concurrently with other code without blocking the execution of the program.
# This is useful for tasks that can take a long time to complete, such as network requests, file I/O, or other I/O operations.
# In Python, you can use the asyncio module to write asynchronous code.

import asyncio

async def read_paper():      # This isn't a function, it's a co-routine
    print("Started Reding Newspaper...")  
    await asyncio.sleep(2)   # Feels same as Multithreading part, but believe me, it's different

    # await keyword is here to simulate the blocking nature of I/O operations
    # But unlike the Multithreading operations, it does not block the main thread, that's the difference

    print("Finished Reading Newspaper...")

asyncio.run(read_paper())