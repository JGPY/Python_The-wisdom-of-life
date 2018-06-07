#Author:Bing Liu

import pygame
import sys
import time
import os
# import logging  # 引入logging模块

class AudioPlay:
    # define of params
    NUM_SAMPLES = 2000
    framerate = 16000
    # paInt16 = 8
    channels = 1
    sampwidth = 2
    # record time
    TIME = 5

    def __init__(self):
        pass

    '''功能：声音播放'''
    def play(self, music_name):
        self.freq = 16000  # audio  quality
        self.bitsize = -16  # unsigned 16 bit
        self.channels = 2  # 1 is mono, 2 is stereo

        self.filePath = r''+music_name
        pygame.mixer.init(self.freq, self.bitsize, self.channels)
        pygame.mixer.music.load(self.filePath)
        pygame.mixer.music.fadeout(1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.stop()

'''
存放于树莓派系统中作为脚本语言运行，
运行脚本时传入的参数为当前目录下的音频文件名
音频格式为mp3格式
'''
if __name__ == '__main__':

    name = ""
    try:
        name = sys.argv[1]
    except Exception as e:
        print("运行脚本时需传入参数，传入的参数为当前目录下的音频文件名,音频格式为mp3格式")
        print(e)
        sys.exit()

    # name.strip()#去掉首尾空格
    # print(os.path)
    # print(os.path.isfile(name+".pm3"))
    # if os.path.isfile(name+".pm3"):
    #     # print(name)
    #     AP = AudioPlay()
    #     # time_start = time.time()
    #     AP.play(name+".mp3")
    #     # ti、me_stop = time.time()
    #     # print("播放用时：", time_stop-time_start,"s")
    # else:
    #     print("当前目录："+os.getcwd()+"不存在 "+name+".mp3 文件")

    try:
        # print(name)
        AP = AudioPlay()
        # time_start = time.time()
        AP.play(name + ".mp3")
        # time_stop = time.time()
        # print("播放用时：", time_stop-time_start,"s")
    except Exception as e:
        print(e)
        sys.exit()
