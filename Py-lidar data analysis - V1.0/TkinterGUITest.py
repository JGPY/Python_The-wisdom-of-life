#Author:Bing Liu

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        master.title("lidar")  # 设置窗口标题
        master.geometry("900x600")  # 设置窗口大小 注意：是x 不是*
        root.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
        tk.Label(root, text="激光雷达数据采集分析系统", bg="pink", font=("楷体", 14), width=88, height=1).pack()


        self.createButton()

    def createButton(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")




if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

