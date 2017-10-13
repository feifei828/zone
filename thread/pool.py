# -*- coding:utf-8 -*-

import time
import threading
from random import random
from queue import Queue
# from multiprocessing.pool import ThreadPool

# pool = ThreadPool(5)
# print(pool.map(lambda x: x**2, range(5)))


def double(n):
    return n * 2


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self._q = queue
        # 守护线程 主线程结束后直接推出，不用等待子线程运行完毕
        self.daemon = True
        self.start()

    def run(self):
        print(self.name)
        while 1:
            f, args, kwargs = self._q.get()
            try:
                print('USE: {}'.format(self.name))
                print(f(*args, **kwargs))
            except Exception as e:
                print(e)
            self._q.task_done()


class ThreadPool(object):
    def __init__(self, num_t=5):
        self._q = Queue(num_t)
        for _ in range(num_t):
            Worker(self._q)

    def add_task(self, f, *args, **kwargs):
        self._q.put((f, args, kwargs))

    def wait_complete(self):
        self._q.join()

pool = ThreadPool()
for _ in range(8):
    wt = random()
    pool.add_task(double, wt)
    time.sleep(wt)
pool.wait_complete()
