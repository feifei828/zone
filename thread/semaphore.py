# -*- coding:utf-8 -*-
import time
from random import random
from threading import Thread, Semaphore

# 限制反问资源数量为3
sema = Semaphore(3)


def foo(tid):
    with sema:
        print('{} acquire sema'.format(tid))
        wt = random() * 2
        time.sleep(wt)
    print('{} realease sema'.format(tid))

threads = []

for i in range(5):
    t = Thread(target=foo, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
