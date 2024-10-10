import time
from threading import Thread

# from tqdm import tqdm

COUNT = 1_000_000_000

def countdown(n):
    # progress = tqdm(total=n, desc='Thread')
    while n>0:
        n -= 1
        # progress.update(1)

# Assuming t1 to t10 are thread objects
thread_count = 16

# Create threads
for tread in range(thread_count):
    t = Thread(target=countdown, args=(COUNT//thread_count,))
    t.start()

start = time.time()

# Join each thread using a loop
for thread in range(thread_count):
    t.join()

end = time.time()

print('Time taken in seconds -', end - start)