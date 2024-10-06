# for i in range(2, 5):
#     print(i)

# from multiprocessing import Semaphore
# import threading
# import time
#
# A = Semaphore(1)
#
#
# def my():
#     global A
#     for i in range(3):
#     # while True:
#     #     A.acquire()
#         time.sleep(1)
#         print("my is : %s" % A)
#
#
# def you():
#     # while True:
#     for j in range(3):
#         A.release()
#         time.sleep(1)
#         print("you is : %s" % A)
#
#
# t2 = threading.Thread(target=you(), args=())
# # time.sleep(3)
# t1 = threading.Thread(target=my(), args=())
# # t2.start()
# # t1.start()

from multiprocessing import Process, Semaphore, Lock, Queue
import time

buffer = Queue(10)  # 创建一个队列用来存放东西
empty = Semaphore(2)  # 生产者的信号
full = Semaphore(0)  # 消费者的信号
lock = Lock()  # 定义一个锁


def 顾客():
    global buffer, empty, full, lock
    # while True:
    for i in range(20):
        # full.acquire()
        full.acquire()
        lock.acquire()
        # buffer.get()
        print('Consumer pop an element')
        print(empty)
        time.sleep(1)
        lock.release()
        empty.release()


def 厂家():
    global buffer, empty, full, lock
    # while True:
    for i in range(2):
        # print((buffer.qsize()))
        empty.acquire()
        # while 1:
        #     c = input("请输入你要改步的信号量值")
        #     empty = Semaphore(int(c))
        #     break
        # lock.acquire()
        # buffer.put(1)
        print('Producer append an element')
        time.sleep(1)
        # lock.release()
        full.release()
        print("Producer"+str(empty))
        print("Consumer"+str(full))


if __name__ == '__main__':
    b = Process(target=厂家, args=())
    # time.sleep(2)
    a = Process(target=顾客, args=())
    b.start()
    a.start()
    b.join()
    a.join()
# a.start()
# b.start()
# if __name__ == '__main__':
#     p = Producer()
#     c = Consumer()
#     p.daemon = c.daemon = True
#     p.start()
#     # c.start()
#     p.join()
#     # c.join()
#     print(full)
#     print('Ended!')
