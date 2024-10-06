# 多进程中优先执行主程序代码 使用类减少代码的重复量
"""
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(0.5)
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))


# 2(0, 1), 3(0, 1, 2), 4(0, 1, 2, 3)

if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        p.start()
        # print(i)
        # time.sleep(10)
"""

# 当daemon如果设置为 True，当父进程结束后，子进程会自动被终止。
"""
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))


if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        p.daemon = True
        p.start()

    print('Main process Ended!')
"""

# 加入 join () 方法即可让我们的子进程运行完之后在运行主程序
"""
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))


if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        p.daemon = True
        p.start()
        p.join()

    print('Main process Ended!')
"""

# 加锁以防各个线程之间并发 保证同一时间只有一个print打印
"""
from multiprocessing import Process, Lock
import time


class MyProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            self.lock.acquire()
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))
            self.lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10, 15):
        p = MyProcess(i, lock)
        p.start()
"""

"""
信号量: Semaphore 用来通知信号
    运用场景: 生产者和消费者
    1. 定义两个信号变量用来通知 生产者和消费者生产和消费
    2. 创建一个队列用来让生产者生产东西和消费者消费东西
    3. 创建一个锁,规定好上锁期间只能允许我这个群体运作
    
"""
#
from multiprocessing import Process, Semaphore, Lock, Queue
import time

buffer = Queue(10)  # 创建一个队列用来存放东西
empty = Semaphore(2)  # 生产者的信号
full = Semaphore(0)  # 消费者的信号
lock = Lock()  # 定义一个锁


class Consumer(Process):

    def run(self):
        global buffer, empty, full, lock
        while True:
            full.acquire()
            lock.acquire()
            buffer.get()
            print('Consumer pop an element')
            print(buffer.qsize())
            time.sleep(1)
            lock.release()
            empty.release()


class Producer(Process):
    def run(self):
        # global buffer, empty, full, lock
        # while True:
        for i in range(2):
            # print((buffer.qsize()))
            empty.acquire()
            lock.acquire()
            buffer.put(1)
            print('Producer append an element')
            time.sleep(1)
            lock.release()
            full.release()
            print(full)


if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print(full)
    print('Ended!')
