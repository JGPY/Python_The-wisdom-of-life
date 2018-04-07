#Author:Bing Liu
#  -*- coding:utf-8 -*-

from tkinter import *
import serial
import serial.tools.list_ports
import SerialPortTest
import time

# define command
device_command = {"header_command": '\xA5', "open_low_power": '\x01', "close_low_power": '\x02',
           "start_module": '\x03', "stop_module": '\x04', "M_state": '\x05',
           "lidar_frequency": '\x0D', "start_lidar": '\x60', "stop_lidar": '\x65',
            "add0.1HZ": '\x09', "add1HZ": '\x0B', "sub0.1HZ": '\x0A', "sub1HZ": '\x0C',
           "restart_device": '\x80', "dev_information": '\x90'}

# function: search serial ports
def find_serial():
    plist = list(serial.tools.list_ports.comports())
    if len(plist) <= 0:
        plist_0 =list("The_Serial_port_can't_find!")
        rx = list("FALSE!")
    else:
        plist_0 = list(plist[0])
        serialName = plist_0[0]
        global serialFd
        serialFd = serial.Serial(serialName, 115200, timeout=2)
        rx = serialFd.readline()
    return rx, plist_0

#function: serial port GUI
def GUI_Tkinter():
    root = Tk()  # 初始化Tk()
    root.title("lidar")  # 设置窗口标题
    root.geometry("900x600")  # 设置窗口大小 注意：是x 不是*
    root.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
    Label(root, text="激光雷达数据采集分析系统", bg="pink", font=("楷体", 14), width=88, height=1).pack()

    # 连接USB串口设备
    def dev_connect():
        rx_0, plist_0 = find_serial()
        t_dev_message.insert(1, plist_0)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    key_connect = Button(root, text="dev_connect", width=10, height=1, command=dev_connect)
    key_connect.place(x=50, y=40, anchor=CENTER)
    t_dev_message = Listbox(root, width=100, height=1)
    t_dev_message.place(x=450, y=40, anchor=CENTER)

    #显示接收信息文本
    Label(root, text="激光雷达反馈数据", bg="pink", font=("楷体", 12), width=31, height=1) \
        .place(x=150, y=67, anchor=CENTER)
    t_lider_message = Text(root, width=40, height=28)
    t_lider_message.place(x=150, y=280, anchor=CENTER)

    #显示按键输入命令文本
    Label(root, text="当前数据发送指令", bg="pink", font=("楷体", 12), width=31, height=1)\
        .place(x=150, y=510, anchor=CENTER)
    Label(root, text="激光雷达控制键", bg="pink", font=("楷体", 12), width=61, height=1) \
        .place(x=580, y=510, anchor=CENTER)
    t_key_message = Text(root, width=40, height=5)
    t_key_message.place(x=150, y=560, anchor=CENTER)

    #按键发送数据显示
    def key_message(comm, fun):
        t_key_message.insert('1.0', "\n命令:", 'end', comm, 'end', "功能：", 'end', fun, 'end', "\n")  # 插入
        t_key_message.delete('3.0', END)   # 删除第三行到最后一行
        pass

    #控制按键功能
    def StartLidar():
        key_message("OxA5 0x60  ", "启动扫描")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["start_lidar"].encode())
        pass

    def LPower():
        key_message("OxA5 0x01  ", "开启低功耗模式")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["open_low_power"].encode())
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    def StartM():
        key_message("OxA5 0x03  ", "启动电机和模组")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["start_module"].encode())
        time.sleep(0.5)
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    def MStatus():
        key_message("OxA5 0x05  ", "电机和模组状态")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["M_state"].encode())
        time.sleep(0.5)
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    def AddxHZ():
        key_message("OxA5 0x09  ", "频率增加0.1HZ")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["add0.1HZ"].encode())
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    def AddxxHZ():
        key_message("OxA5 0x0C  ", "频率增加1HZ")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["add1HZ"].encode())
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    def Restart():
        key_message("OxA5 0x80  ", "重启设备")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["restart_device"].encode())
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    def StopLidar():
        key_message("OxA5 0x65  ", "停止扫描")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["stop_lidar"].encode())
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')
        run_rx=False

    def NLpower():
        key_message("OxA5 0x02  ", "关闭低功耗模式")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["close_low_power"].encode())
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    def StopM():
        key_message("OxA5 0x03  ", "关闭电机和模组")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["start_module"].encode())
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    def Frequency():
        key_message("OxA5 0x0D  ", "获取当前频率")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["dev_information"].encode())
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    def SubxHZ():
        key_message("OxA5 0x09  ", "频率减少0.1HZ")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["sub0.1HZ"].encode())
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    def SubxxHZ():
        key_message("OxA5 0x0C  ", "频率减少1HZ")
        serialFd.write(device_command["header_command"].encode())
        serialFd.write(device_command["sub1HZ"].encode())
        rx = serialFd.readline()
        rx_0 = list(rx)
        t_lider_message.insert('1.0', rx_0, END, '\n')

    # 创建按钮
    Button(root, text="StartLidar", width=10, height=1, command=StartLidar).place(x=340, y=540, anchor=CENTER)
    Button(root, text="LPower", width=10, height=1, command=LPower).place(x=420, y=540, anchor=CENTER)
    Button(root, text="StartM", width=10, height=1, command=StartM).place(x=500, y=540, anchor=CENTER)
    Button(root, text="MStatus", width=10, height=1, command=MStatus).place(x=580, y=540, anchor=CENTER)
    Button(root, text="Add0.1HZ", width=10, height=1, command=AddxHZ).place(x=660, y=540, anchor=CENTER)
    Button(root, text="Add1HZ", width=10, height=1, command=AddxxHZ).place(x=740, y=540, anchor=CENTER)
    Button(root, text="Restart", width=10, height=1, command=Restart).place(x=820, y=540, anchor=CENTER)

    Button(root, text="StopLidar", width=10, height=1, command=StopLidar).place(x=340, y=580, anchor=CENTER)
    Button(root, text="NLpower", width=10, height=1, command=NLpower).place(x=420, y=580, anchor=CENTER)
    Button(root, text="StopM", width=10, height=1, command=StopM).place(x=500, y=580, anchor=CENTER)
    Button(root, text="Frequency", width=10, height=1, command=Frequency).place(x=580, y=580, anchor=CENTER)
    Button(root, text="Sub 0.1HZ", width=10, height=1, command=SubxHZ).place(x=660, y=580, anchor=CENTER)
    Button(root, text="Sub 1HZ", width=10, height=1, command=SubxxHZ).place(x=740, y=580, anchor=CENTER)
    Button(root, text="", width=10, height=1).place(x=820, y=580, anchor=CENTER)

    root.mainloop()  # 进入消息循环

if __name__ == "__main__":
    GUI_Tkinter()




