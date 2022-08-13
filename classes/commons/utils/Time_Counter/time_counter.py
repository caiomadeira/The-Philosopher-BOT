import time
import threading

def stopwatch():
    start = time.time()

    for i in range(10):
        print("Test")
        time.sleep(1)

    end = time.time()
    elapsed = end - start
    elapsed = int(elapsed)

    print("Executado em", elapsed, "segundos")

def count(seconds):
    for number in range(1, seconds):
        time.sleep(1)
        print(f'{number} Segundos restantes')

