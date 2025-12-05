# Now, can Async and MultiProcessing work together?
# Answer: Yes, you will understand it better when you see the code

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f"{data[::-1]} Encrypted!"     # Basically reversing the string

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt, "My_Super_Secret")
        print(f"{result}")

# If you are delaing with the processes, the main routine is always is required
if __name__ == "__main__":
    asyncio.run(main())