#-*-coding:utf-8-*-
#客户端程序
import socket    #导入socket模块
import threading
outString = ''
nick = ''
inString = ''
def client_send(sock):
    global outString
    while True:
        outString = input()   #接收输入
        outString = nick+':'+outString
        sock.send(outString.encode())

def client_accept(sock):
    global inString
    while True:
        try:
            inString = sock.recv(1024)  #接收数据
            if not inString:
                break
            if outString != inString:
                print(inString)
        except:
            break
nick = input('输入你的名字：')
ip = input('输入IP地址：')
port = 8888
sock = socket.socket()   #创建套接字
sock.connect((ip, port))  #连接
sock.send(nick.encode())     #把用户名发送给服务端
th_send = threading.Thread(target=client_send, args=(sock,))   #发送消息的线程
th_send.start()
th_accept = threading.Thread(target=client_accept, args=(sock,))
th_accept.start()


