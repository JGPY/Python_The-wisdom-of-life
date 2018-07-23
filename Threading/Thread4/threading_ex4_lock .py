#Author:Liu Bing

'''
python GIL vs  thread Lock
'''

import threading
import time

def run(n):
    lock.acquire() #加锁后，程序变串行
    global num
    num += 1
    time.sleep(1)
    lock.release()


lock = threading.Lock()
num = 0
start_time = time.time()
t_objs = []
for i in range(5):
    t = threading.Thread(target=run, args=("t-%s" % i, ))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print("---------all threads has finished")
print("num:", num)
print("cost:", time.time()-start_time)
