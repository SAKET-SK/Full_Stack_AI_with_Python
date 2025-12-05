# Handling Asychnronous Web Requests

import asyncio
import aiohttp      # will need venv for this, pip install aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls=["http://httpbin.org/delay/2", "http://httpbin.org/delay/3"] * 2
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)     # A shorthand notation for unpacking things in python

asyncio.run(main())

