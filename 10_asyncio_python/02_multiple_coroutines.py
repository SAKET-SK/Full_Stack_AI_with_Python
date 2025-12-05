import asyncio
# import time

async def read_paper(page_name):
    print(f"Started reading {page_name} page from newspaper ...")
    await asyncio.sleep(2)
    # time.sleep(2)       # Un-comment this to see the difference...
    print(f"Finished reading {page_name} page from newspaper ...")

async def main():    # it can be named anything
    await asyncio.gather(read_paper("Sports"), read_paper("Technology"), read_paper("Lifestyle"))
    # gather() method wraps all co-routines in a future and scheduled in an Event Loop. Order can change.
    # All futures must share the same event loop

asyncio.run(main())

# After execution of this code, you will notice we waited combiningly for 2 seconds. (As passed above)
# Because this is a non-blocking operation