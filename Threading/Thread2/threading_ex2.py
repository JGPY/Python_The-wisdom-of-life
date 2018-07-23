#Author:Liu Bing

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        print("runint task：", self.n)
        time.sleep(2)
        print("runint task：", self.n)


t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()
# t1.join() #=wait()
t2.start()

