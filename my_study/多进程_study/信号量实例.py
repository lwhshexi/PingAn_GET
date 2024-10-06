# from multiprocessing import Lock, Queue, Semaphore, Process
# import time
# """
# 信号量: Semaphore 用来通知信号
#     运用场景: 生产者和消费者
#     1. 定义两个信号变量用来通知 生产者和消费者生产和消费
#     2. 创建一个队列用来让生产者生产东西和消费者消费东西
#     3. 创建一个锁,规定好上锁期间只能允许我这个群体运作
#
# """
# 仓库 = Queue(10)
# lock = Lock()
# 生产者 = Semaphore(2)
# 消费者 = Semaphore(3)
#
#
# class gk(Process):
#     def run(self):
#         global 仓库, 生产者, 消费者, lock
#         while True:
#             生产者.acquire()
#             # 消费者.acquire()  # 信号值为0会阻塞
#             print("我是消费者"+time.strftime('%H:%M:%S'))
#             # print(消费者)
#             time.sleep(1)
#
#
# class scz(Process):
#     def run(self):
#         global 仓库, 生产者, 消费者, lock
#         while True:
#             生产者.acquire()
#             print("我是生产者"+time.strftime('%H:%M:%S'))
#             time.sleep(1)
#             # 消费者.release()
#             # print(消费者)
#
#
# if __name__ == '__main__':
#     b = scz()
#     c = scz()
#     a = gk()
#     c.start()
#     b.start()
#     a.start()
#     # time.sleep(4)

from multiprocessing import Process, Semaphore
import time


def scz(id, a1):
    a1.acquire()
    # print(a1)
    print(f"{id} 生产了一个商品! {time.strftime('%H:%M:%S')}")  # 正确的时间格式
    time.sleep(2)
    a1.release()
    print(f"{id} 出售了一个商品! {time.strftime('%H:%M:%S')}")  # 正确的时间格式


if __name__ == "__main__":
    a1 = Semaphore(3)
    for i in range(10):
        t1 = Process(target=scz, args=(i, a1))
        t1.start()

