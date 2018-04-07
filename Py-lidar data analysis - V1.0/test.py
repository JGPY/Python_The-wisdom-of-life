# #Author:Bing Liu
#
# import threading #导入threading
# import time
#
# import threading
# from time import ctime,sleep
#
#
# def music(func):
#     for i in range(2):
#         sleep(2)
#         print ("I was listening to %s. %s" %(func,ctime()))
#
#
# def move(func):
#     for i in range(2):
#         sleep(1)
#         print ("I was at the %s! %s" %(func,ctime()))
#
#
# threads = []
# t1 = threading.Thread(target=music,args=(u'爱情买卖',))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#     sleep(12)
#     print ("all over %s" %ctime())
#

#
# mygenerator = (x*x for x in range(4))
# for i in mygenerator:
#     for i in mygenerator:
#         print('n=:',i)
#     print('i=:',i)
#
# def createGenerator():
#     mylist = range(3)
#     for i in mylist:
#         yield i*i
#         yield i
#
# mygenerator = createGenerator()  # create a generator
# print(mygenerator)  #  mygenerator is an object!
#
# for i in mygenerator:
#     print(i)
# import re
#
# key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
# p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
# pattern1 = re.compile(p1)#我们在编译这段正则表达式
# matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
# print(matcher1.group(0))#打印出来
#
# key = r"javapythonhtmlvhdl"#这是源文本
# p1 = r"python"#这是我们写的正则表达式
# pattern1 = re.compile(p1)#同样是编译
# matcher1 = re.search(pattern1,key)#同样是查询
# print(matcher1.group(0))
#
# key = r"<h1>hello world<h1>"#源文本
# p1 = r"<h1>.+<h1>"#我们写的正则表达式，下面会将为什么
# pattern1 = re.compile(p1)
# print(pattern1.findall(key))#发没发现，我怎么写成findall了？咋变了呢？
#
#
# key = r"afiouwehrfuichuxiuhong@hit.edu.cnaskdjhfiosueh"
# p1 = r"chuxiuhong@hit\.edu\.cn"
# pattern1 = re.compile(p1)
# print(pattern1.findall(key))
#
# key = r"http://www.nsfbuhwe.com and https://www.auhfisna.com"#胡编乱造的网址，别在意
# p1 = r"https*://"#看那个星号！
# pattern1 = re.compile(p1)
# print(pattern1.findall(key))


def Calc(t_int):
    if t_int <= 1:
        return False
    for i in range(2, t_int):
        if t_int % i == 0:
            return False
    return True

if __name__ == '__main__':
    a = range(0, 100)
    print(type(a))
    print(a)
    print(a[0], a[1])
    while True:
        n = input()
        print(Calc(int(n)))
