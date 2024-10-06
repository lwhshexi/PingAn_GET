import multiprocessing
x = 4
y = multiprocessing.Semaphore(3)


def my():
    # global x
    x = 8
    y.acquire()
    print("x = ", x)
    print(y)


print("x = ", x)
print(y)
my()
print("x = ", x)
print(y)
