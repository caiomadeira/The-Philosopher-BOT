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


def count(start, stop):
    cont_range = range(start, stop)
    for number in reversed(cont_range):
        time.sleep(1)
        print(f'{number} Segundos restantes')


count(0, 11)
