"""
Create a decorator function that prints the time taken by a function to execute.
"""

import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Time taken in seconds - {end - start:.2f}')
    return wrapper
