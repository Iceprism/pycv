import cv2
import numpy as np
import matplotlib.pyplot as plt

# 上一版本成功验证正常图片情况
# 开始测试实际情况，使用5条线进行取样平均，获得新的线
# 测试通过，下一步将增加缺线即剔除，将缺少上边缘或者下边缘的线剔除掉


src = cv2.imread("test2.jpg")
cv2.imshow("src1", src)
rows, cols, channels = src.shape
redsrc = src.copy()
redsrc = src[:, :, 2]
cv2.imshow("redsrc", redsrc)
img = redsrc.copy()
dst = redsrc.copy()
srcLine = src.copy()

a = 1.3
b = 0
for i in range(rows):
    for j in range(cols):
        color = img[i, j] * a + b
        if color > 255:
            dst[i, j] = 255
        else:
            dst[i, j] = color

cv2.imshow('dst', dst)
listPixavr = []
listPix20 = []
listPix30 = []
listPix40 = []
listPix50 = []
listPix60 = []

for i in range(0, rows):
    color = dst[i, 20]
    listPix20.append(color)
    color = dst[i, 40]
    listPix30.append(color)
    color = dst[i, 80]
    listPix40.append(color)
    color = dst[i, 100]
    listPix50.append(color)
    color = dst[i, 120]
    listPix60.append(color)

# print(listPix)
for i in range(len(listPix20)):
    listPixavr.append(int((int(listPix20[i])+int(listPix30[i])+int(listPix40[i])+int(listPix50[i])+int(listPix60[i]))/5))



lastPix = []
lastPixT = []
lastPixD = []

for i in range(0, len(listPixavr) - 1):
    subPix = int(listPixavr[i + 1]) - int(listPixavr[i])
    if subPix > 20:
        print(i)
        lastPix.append(i)
        lastPixT.append(i)
    if subPix < -20:
        print(i)
        lastPix.append(i)
        lastPixD.append(i)

print(lastPix, lastPixT, lastPixD)
for j in range(4):
    for i in range(len(lastPix)):
        try:
            if lastPix[i + 1] - lastPix[i] < 5:
                lastPix.remove(lastPix[i + 1])
        except IndexError:
            pass

print(lastPix)
print("24:", listPixavr[24], listPixavr[25], listPixavr[26])

for i in range(len(lastPix)):
    lastPix[i] = lastPix[i] + 1
    if i % 2 == 1:
        avrline = int((lastPix[i] - lastPix[i - 1]) / 2 + lastPix[i - 1])
        for j in range(cols):
            srcLine[avrline, j] = [255, 255, 0]
    for j in range(cols):
        srcLine[lastPix[i], j] = [0, 255, 0]

srcLineRed = srcLine[:, :, 2]

for i in range(rows):
    srcLine[i,20] = [255,0,0]
    srcLine[i, 40] = [255, 0, 0]
    srcLine[i, 80] = [255, 0, 0]
    srcLine[i, 100] = [255, 0, 0]
    srcLine[i, 120] = [255, 0, 0]


cv2.imshow("srcLine", srcLine)
cv2.imwrite("srcLine.jpg", srcLine)

file = open('listex.txt', 'w', encoding='utf-8')
for i in range(len(listPix20)):
    file.write(str(listPix20[i]) + ';' + str(listPix30[i]) + ';' + str(listPix40[i]) + ';' + str(listPix50[i]) + ';' + str(listPix60[i]) + '\r')
file.close()
cv2.waitKey()
