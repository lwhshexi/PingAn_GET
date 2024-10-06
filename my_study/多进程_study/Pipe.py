"""
管子的单工类似于queue,双工的话 管子的只能接收另一端发送的消息.
"""
from multiprocessing import Process, Pipe


class Consumer(Process):
    def __init__(self, pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        self.pipe.send('Consumer Words')
        print('Consumer Received:', self.pipe.recv())


class Producer(Process):
    def __init__(self, pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        print('Producer Received:', self.pipe.recv())
        self.pipe.send('Producer Words')


if __name__ == '__main__':
    pipe = Pipe()
    p = Producer(pipe[1])
    c = Consumer(pipe[0])
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Ended!')
