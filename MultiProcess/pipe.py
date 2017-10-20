# -*- coding:utf-8 -*-
from multiprocessing import Process, Pipe, Pool

"""
进程间通信，管道
子链接传输，夫链接接收
"""


def f(conn):
    conn.send(['hello'])
    conn.close()

# parent_conn, child_conn = Pipe()
# p = Process(target=f, args=(child_conn,))
# p.start()
# print(parent_conn.recv())
# p.join()


def spawn(f):
    def func(pipe, item):
        pipe.send(f(item))
        pipe.close()
    return func


def parmap(f, items):
    pipe = [Pipe() for _ in items]
    proc = [Process(target=spawn(f), args=(child, item))
            for item, (parent, child) in zip(items, pipe)]
    [(p.start(), p.join()) for p in proc]
    return [parent.recv() for (parent, child) in pipe]


class CalculateFib(object):
    @classmethod
    def fib(cls, n):
        if n <= 2:
            return 1
        return cls.fib(n-1) + cls.fib(n-2)

    def map_run(self):
        pool = Pool(2)
        print(pool.map(self.fib, [35] * 2))

    def parmap_run(self):
        print(parmap(self.fib, [35] * 2))

cl = CalculateFib()
cl.map_run()
cl.parmap_run()