#Python threads are real OS-level threads, so they are "heavyweight", but provide full concurrency.

import threading
from threading import Thread
import time


def threadfunc():
    print("Thread started")
    time.sleep(5)
    print("Thread finished")

print(threading.active_count())

thrd = Thread(target=threadfunc)
thrd.start()
thrd.join()
print(threading.active_count())

#GIL - Global Interpreter Lock
#GIL is a mutex that protects access to Python objects,
# preventing multiple threads from executing Python bytecodes at once.

kill_thread = False

def working_thread():
    while True:
        if kill_thread == True:
           return

thrd = Thread(target=working_thread)
threading.active_count()
thrd.start()
kill_thread = True


