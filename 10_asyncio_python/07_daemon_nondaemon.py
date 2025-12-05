# daemon and non daemon threads

# Daemon threads are the background threads which automaically shuts down when the main program is over.
# Used for non critical background tasks like logging and monitoring.

import threading
import time

def monitor_temp():
    while True:
        print(f"Monitoring temperature...")
        time.sleep(2)

# To make a non-daemon version, simply remove the daemon=True. This will make it go in infinite loop, even though my main program is over.
t = threading.Thread(target=monitor_temp, daemon=True)   
t.start()

print("Main program finished...")