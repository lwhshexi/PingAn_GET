# import queue
#
# a = queue.LifoQueue(10)  # 先入后出
# # a = queue.Queue(10)  # 先入先出
# b = ['1', '2', '3', '4']
# for d in b:
#     c = a.put(d)
#
# for i in range(4):
#     e = a.get()
#     print(e)
#     print("大小为: %s" % a.qsize())


import multiprocessing
import time


def worker(s, i, name):
    s.acquire()  # 获得锁
    print(time.strftime('%H:%M:%S'), multiprocessing.current_process().name + " 获得锁运行 "+name);
    time.sleep(i)
    print(time.strftime('%H:%M:%S'), multiprocessing.current_process().name + " 释放锁结束 "+name);
    s.release()  # 释放锁


if __name__ == "__main__":
    s = multiprocessing.Semaphore(2)
    for i in range(6):
        print(1)
        p = multiprocessing.Process(target=worker, args=(s, 2, str(i)))
        p.start()
