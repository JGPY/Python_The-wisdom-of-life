#Author:Bing Liu

import serial
import serial.tools.list_ports
import threading
import time

class MSerialPort:
    message = ''
    def __init__(self, port, buandRate=115000, timeOut=2):
        self.port = serial.Serial(port, buandRate, timeout=timeOut)
        if not self.port.isOpen():
            self.port.open()
    def portOpen(self):
        if not self.port.isOpen():
            self.port.open()
    def portClose(self):
        self.port.close()
    def sendData(self,data):
        number = self.port.write(data)
        return number
    def readData(self):
        while True:
            data = self.port.readline()
            self.message = data

if __name__ == '__main__':
    mSerial = MSerialPort('COM3', 115000)
    threading.Thread(target=mSerial.readData).start()

    while True:
        time.sleep(3)
        mSerial.sendData('\xA5\x60'.encode())
        print(mSerial.message)
        mSerial.message = None
        print('next line')
