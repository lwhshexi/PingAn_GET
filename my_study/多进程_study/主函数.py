from multiprocessing import Process, Semaphore
import time


def a(name, c):
    id_name = name
    c.acquire()
    print(id_name + "已经获取锁" + id_name + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(2)
    print(id_name + "已经释放锁" + id_name + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    c.release()


if __name__ == '__main__':
    c = Semaphore(2)
    for j in range(5):
        # print(1)
        name1 = Process(target=a, args=(str(j), c))
        name1.start()

# t2 = Process(target=b(), args=())

# import multiprocessing
# import time
#
#
# def a(name, c, i):
#     c.acquire()  # 获得锁
#     print(time.strftime('%H:%M:%S'), multiprocessing.current_process().name + " 获得锁运行 " + name);
#     time.sleep(i)
#     print(time.strftime('%H:%M:%S'), multiprocessing.current_process().name + " 释放锁结束 " + name);
#     c.release()  # 释放锁
#
#
# # def b():
# #     c.release()
# #     print("hello")
# #     print_current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# #     print("b " + print_current_time)
#
# if __name__ == '__main__':
#     c = multiprocessing.Semaphore(2)
#     for i in range(6):
#         print(1)
#         p = multiprocessing.Process(target=a, args=(str(i), c, i))
#         p.start()
