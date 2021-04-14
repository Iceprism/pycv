# coding=utf-8
# 说明：
# v2，重构代码
#

# 导入库
import cv2
import numpy as np
import matplotlib.pyplot as plt
import serial
import time


def Re_serialPort():
    # 开启串口，由于开启串口会使arduino-nano重启，所以sleep等单片机正常
    serialPort="COM5"
    baudRate=9600
    ser=serial.Serial(serialPort, baudRate, timeout=1)
    time.sleep(0.8)  # 等单片机正常 0.8s

def
    MicaPic = cv2.imread("../img/w1.png")
    croppedsrc = MicaPic[371:463, 0:512]
    cv2.imwrite("cutsrc.jpg",croppedsrc)
    plt.figure("res")
    plt.subplot(121)
    plt.imshow(MicaPic)

