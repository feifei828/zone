# -*- coding:utf-8 -*-

"""
多进程 & 多线程 是否资源共享
线程安全保证多个线程同时执行程序依旧运行正确
GIL 线程锁
每一个进程只能同时仅有一个线程来执行
"""
import time
import threading


def profile(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('COST: {}'.format(end - start))
    return wrapper


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n -2)


@profile
def nothreading():
    fib(35)
    fib(35)


@profile
def hastreading():
    threads = []
    for i in range(2):
        t = threading.Thread(target=fib, args=(35,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


nothreading()
hastreading()

