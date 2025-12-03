# Downloading images using Threads

import threading
import time

import requests  # Need venv for this

# python -m venv venv  -> Create venv
# .\venv\Scripts\Activate.ps1  -> Activate venv
# pip install requests  -> Install requests in venv

def download(url):
    print(f"Started Downloading from {url}...")
    resp = requests.get(url)
    print(f"Completed Downloading from {url}...Size is {len(resp.content)} bytes")  # resp.content is ONLY in bytes

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]

start = time.time()
threads = []       # [] is a list of threads

for url in urls:
    t = threading.Thread(target=download, args=(url,))   # Since the args are in tuple format, make sure to place the extra comma
    threads.append(t)      # Add each thread to the list - this is an array of threads
    t.start()

for t in threads:
    t.join()

end = time.time()
print(f"Total Execution Time : {end - start:.2f} seconds")

# Threads actually shine when operations are I/O-bound, such as disk read/write or web requests from the internet.
