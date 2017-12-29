#-*-coding:utf-8-*-
import socket
import threading
import time

LockCondtion = threading.Condition()
s = socket.socket()
host = input("请输入服务器IP地址:")
port = 9000
data = ''
print("服务器创建成功！")
s.bind((host, port))
s.listen(3)   #监听请求,假设有9个请求，先处理3个，在处理剩余的
'''
队列：【1,2,3】456789
      【2,3,4】56789
      【3,4,5】6789
      ...
'''

def NewClient():
    global connection
    global buf
    while True:
        connection, address = s.accept()    #接收到连接了 addr包含ip和port
        print('Connected with '+address[0]+':'+str(address[1]))
        buf = connection.recv(1024)
        NotifyAll('欢迎'+bytes.decode(buf)+'来到聊天室！')
        print(data)
        connection.send(data.encode())#发送至各客户端

def NotifyAll(data1):
    global data
    if LockCondtion.acquire():
        data = data1
        LockCondtion.notifyAll()
        LockCondtion.release()

def threadOut(conn):  #发送消息
    global data
    while True:
        if LockCondtion.acquire():
            LockCondtion.wait()   #放弃对当前资源的占有
            if data:
                try:
                    conn.send(data)
                    LockCondtion.release()
                except:
                    LockCondtion.release()
                    return


def threadIn(conn, buf):   #接收消息
    while True:
        print("threadIn")
        try:
            temp = conn.recv(2014)
            print("threadIn2")
            if not temp:
                conn.close()
                return
            NotifyAll(temp)
            print(data)
        except:
            NotifyAll(buf+'error')
            print(data)
            return


if __name__ == '__main__':
    threading.Thread(target=NewClient()).start()
    threading.Thread(target=threadOut, args=connection).start()
    threading.Thread(target=threadIn, args=(connection, buf)).start()

    while 1:
        time.sleep(1)
        pass

    s.close
    print("!")


