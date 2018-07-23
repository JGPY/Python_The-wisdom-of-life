#Author:Liu Bing

import threading
import time

def run(n):
    print("task:", n, threading.active_count())
    time.sleep(2)
    print("task done:", n, threading.current_thread(),)

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" %i,))
    '''主线程不是守护线程，程序等待主线程执行完毕，但不等待其余50个守护线程'''
    t.setDaemon(True) #把当前线程设置守护线程,已激活的线程不能设置  Java启动的 线程默认为守护线程
    t.start()
    t_objs.append(t)
#
# for t in t_objs:
#     t.join()

print("---------all threads has finished", threading.current_thread(), threading.active_count())
print("cost:", time.time()-start_time)
