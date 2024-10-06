from multiprocessing import Process, Semaphore, Lock, Queue
import time
from random import random

buffer = Queue(10)
empty = Semaphore(2)
full = Semaphore(0)
lock = Lock()


def Consumer(buffer, empty, full, lock):
    while True:
        full.acquire()
        lock.acquire()
        print('Consumer get', buffer.get())
        time.sleep(1)
        lock.release()
        empty.release()


def Producer(buffer, empty, full, lock):
    while True:
        empty.acquire()
        lock.acquire()
        num = random()
        print('Producer put ', num)
        buffer.put(num)
        time.sleep(1)
        lock.release()
        full.release()


if __name__ == '__main__':
    p = Process(target=Producer, args=(buffer, empty, full, lock))
    c = Process(target=Consumer, args=(buffer, empty, full, lock))
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Ended!')
