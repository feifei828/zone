import time
from multiprocessing import Process, JoinableQueue, Queue
from random import random

tasks_queue = JoinableQueue()
results_queue = Queue()
