"""
This script creates multiple threads to run the same function.
"""
import threading
from time import sleep

def print_message(x):
    for i in range(x):
        sleep(1)
        print(f'Mensaje {x}: {i + 1} segundo(s)')
    print(f'---> {x} terminado')

def main():
    threads = []
    for i in range(20):
        t = threading.Thread(target=print_message, args=(i + 1,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        print('-->Thread finished<--')

main()
