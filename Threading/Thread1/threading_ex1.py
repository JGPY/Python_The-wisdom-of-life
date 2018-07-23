#Author:Liu Bing

import threading
import time

def run(n):
    print("task:", n)
    time.sleep(2)
    print("task:", n)

t1 = threading.Thread(target=run, args=("t1",))
t2 = threading.Thread(target=run, args=("t2",))
# t1 = threading.Thread(target=run("t1"))
# t2 = threading.Thread(target=run("t2"))
t1.start()
t2.start()
