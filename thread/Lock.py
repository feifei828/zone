# -*- coding:utf-8 -*-

import time
from threading import Thread, Lock

nolock_value = 0
haslock_value = 0
lock = Lock()


def nolock(i):
    global nolock_value
    print('{} nolock start {}'.format(i, nolock_value))
    new = nolock_value + 1
    time.sleep(0.001)
    nolock_value = new
    print('{} nolock end {}'.format(i, nolock_value))


def haslock(i):
    global haslock_value
    with lock:
        print('{} haslock start {}'.format(i, haslock_value))
        new = haslock_value + 1
        time.sleep(0.001)
        haslock_value = new
        print('{} haslock end {}'.format(i, haslock_value))

threads = []

for i in range(100):
    t = Thread(target=nolock, args=(i,))
    t.start()
    threads.append(t)

for i in range(100):
    t = Thread(target=haslock, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(nolock_value)
print(haslock_value)
