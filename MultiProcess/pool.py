# -*- coding:utf-8 -*-

import time
from multiprocessing import Pool, current_process

"""
 pool.apply_async().get() = pool.apply()
"""


def profile(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('COST: {}'.format(end - start))
    return wrapper


def fib(n):
    print('{} start:{}'.format(current_process().name, n))
    time.sleep(1)
    print('{} end:{}'.format(current_process().name, n))


@profile
def ApplyAsync():
    pool = Pool(4)
    for i in range(10):
        pool.apply_async(fib, (35,)).get()
    pool.close()
    pool.join()


@profile
def Apply():
    pool = Pool(4)
    for i in range(10):
        pool.apply(fib, (35,))
    pool.close()
    pool.join()



Apply()
ApplyAsync()
