"""
# Myclass家族，但是这个家族只有一个人f
class MyClass:
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)  # 家族x + 物品名i
print("MyClass 类的方法 f 输出为：", x.f())  # 家族x + 人名f

"""  # 一个简单的类实例

"""
# class Complex:
#     def __init__(self, realpart, imagpart):  # 必须要有一个self参数，
#         self.r = realpart
#         self.i = imagpart
# 
# 
# x = Complex(3.0, -4.5)
# print(x.r, x.i)  # 输出结果：3.0 -4.5
"""  # 类实例化

"""
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0

    # 定义私有属性,私有属性在类外部无法直接进行访问
    # 定义构造方法
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('Python', 10)
p.speak()
"""  # 调用类里的函数

"""
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):  # student为子类，people为父类
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()
"""  # 继承类方法

from multiprocessing import Process, Semaphore
import time

a = Semaphore(1)


def method1(age, a):
    a.acquire()
    print(f"我是method1, 我的年纪是{age} {time.strftime('%H:%M:%S')}")
    time.sleep(2)
    a.release()


if __name__ == "__main__":
    for i in range(3):
        print(1)
        t1 = Process(target=method1, args=(i, a))
        t1.start()
