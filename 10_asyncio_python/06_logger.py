# Some fun stuff!!

import asyncio
import threading
import time

def background_logger():
    while True:
        time.sleep(1)
        print("Background logger is running...")

async def fetch_data():
    await asyncio.sleep(2)
    print("Fetched the data...")

# Both of these guys will not bother each other....

threading.Thread(target=background_logger, daemon=True).start()
asyncio.run(fetch_data())