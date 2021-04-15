import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# 将缺少上边缘或者下边缘的线剔除掉，
# 选择上下线策略优化，判断前后线有无
# 去除对比度增强，执行效率提升，0.01s一帧 原0.28s一帧
# 改写取样函数

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


dst = img.copy()

time_start=time.time()

listPixavr = []
listPix20 = []
listPix30 = []
listPix40 = []
listPix50 = []
listPix60 = []



# print(listPix)
# for i in range(len(listPix20)):
#     listPixavr.append(int((int(listPix20[i])+int(listPix30[i])+int(listPix40[i])+int(listPix50[i])+int(listPix60[i]))/5))

# 重构建取样函数

def getAvrPix():
    sampelLine = []
    x = 50
    color = 0
    for i in range(12):
        x = x + 15
        sampelLine.append(x)
        # print(sampelLine)

    for i in range(0, rows):
        for j in range(len(sampelLine)):
            color = color + int(dst[i, j])
        color = int(color/12)
        listPixavr.append(color)

getAvrPix()

lastPix = []
lastPixT = []
lastPixD = []

for i in range(0, len(listPixavr) - 1):
    subPix = int(listPixavr[i + 1]) - int(listPixavr[i])
    if subPix > 21:
        print(i)
        lastPix.append(i)
        lastPixT.append(i)
    if subPix < -27:
        print(i)
        lastPix.append(i)
        lastPixD.append(i)

print(lastPix, lastPixT, lastPixD)
for j in range(4):
    for i in range(len(lastPix)):
        try:
            localPix = lastPix[i]
            print(localPix)
            if i % 2 == 0:
                if lastPix[i + 1] - lastPix[i] > 20:
                    lastPix.remove(lastPix[i])
            if lastPix[i] - lastPix[i-1] >20 :  # 前面无线
                if lastPix[i + 1] - lastPix[i] < 5:
                    lastPix.remove(lastPix[i + 1]) # 减去i+1 这条线
            if lastPix[i] - lastPix[i-1] <20 :
                if lastPix[i + 1] - lastPix[i] < 5:
                    lastPix.remove(lastPix[i]) # 减去i 这条线

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

time_end=time.time()
print('totally cost',time_end-time_start)

cv2.imshow("srcLine", srcLine)
cv2.imwrite("srcLine.jpg", srcLine)


file = open('listex.txt', 'w', encoding='utf-8')
for i in range(len(listPix20)):
    file.write(str(listPix20[i]) + ';' + str(listPix30[i]) + ';' + str(listPix40[i]) + ';' + str(listPix50[i]) + ';' + str(listPix60[i]) + '\r')
file.close()

cv2.waitKey()
