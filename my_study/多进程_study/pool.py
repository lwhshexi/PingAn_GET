"""
非阻塞:
from multiprocessing import Lock, Pool
import time


def function(index):
    print('Start process: ', index)
    time.sleep(3)
    print('End process', index)


if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in range(4):
        pool.apply_async(function, (i,))

    print("Started processes")
    pool.close()
    pool.join()
    print("Subprocess done.")
"""
# apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞，apply(func[, args[, kwds]]) 是阻塞的。
from multiprocessing import Lock, Pool
import time


def function(index):
    print('Start process: ', index)
    time.sleep(3)
    print('End process', index)


if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in range(4):
        pool.apply(function, (i,))

    print("Started processes")
    pool.close()
    pool.join()
    print("Subprocess done.")
