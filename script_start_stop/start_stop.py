#!/usr/bin/python
#Author:Liu Bing

import os, sys, time, subprocess


_program = '*****.jar'  ##项目 jar 包
_daemon = '*********.py'  ## 脚本名称


def getProgramPid():

    result = subprocess.getoutput("ps aux | grep java | grep %s | grep -v grep | awk '{print $2}'" % _program)
    return result


def getDaemonPid():

    result = subprocess.getoutput("ps aux | grep python | grep '%s monitor' | grep -v grep | awk '{print $2}'" % _daemon)
    return result


def startProgram():

    p_pid = getProgramPid()
    if p_pid != '':
        print('It seems this program is already running...')
    else:
        print('Starting program...')
    if os.system('nohup java -jar %s appService >> log/FeiGuo.log 2>&1 &' % _program) == 0:
        print('start program successfully and pid is ' + getProgramPid())


def startDaemon():

    d_pid = getDaemonPid()
    if d_pid != '':
        print('It seems this daemon is already running...')
    else:
        print('Starting daemon...')
    if os.system('nohup python %s monitor >> log/daemon.log 2>&1 &' % _daemon) == 0:
        print('start daemon successfully and pid is ' + getDaemonPid())


def stopProgram():

    p_pid = getProgramPid()
    if p_pid == '':
        print('It seems this program is not running...')
    else:
        os.system('kill -9 ' + p_pid)
    print('program stopped')


def stopDaemon():

    d_pid = getDaemonPid()
    if d_pid == '':
        print('It seems daemon is not running...')
    else:
        os.system('kill -9 ' + d_pid)
    print('daemon stopped')


def monitor():

    while 1:
        time.sleep(10)
        p_pid = getProgramPid()
        if p_pid == '':
            print('It seems this program is not running. Start it now!')
            startProgram()


if __name__ == '__main__':

    if (len(sys.argv) == 2):
        args = sys.argv[1]
    else:
        args = input('Enter args: ')
        logPath = os.path.curdir + os.sep + 'log'
    if not os.path.exists(logPath):
        os.mkdir(logPath)
    if args == 'start':
        startProgram()
        startDaemon()
    elif args == 'stop':
        stopDaemon()
        stopProgram()
    elif args == 'restart':
        stopDaemon()
        stopProgram()
        time.sleep(3)
        startProgram()
        startDaemon()
    elif args == 'monitor':
        monitor()
    else:
        print('nothing to do')

