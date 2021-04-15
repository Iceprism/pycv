import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("test.png")
cv2.imshow("src1", src)
rows, cols, channels = src.shape
redsrc = src.copy()
redsrc = src[:, :, 2]
cv2.imshow("redsrc", redsrc)
img = redsrc.copy()
dst = redsrc.copy()
srcLine = src.copy()

a = 0.8
b = 50
for i in range(rows):
    for j in range(cols):
        color = img[i, j] * a + b
        if color > 255:
            dst[i, j] = 255
        else:
            dst[i, j] = color

cv2.imshow('dst', dst)

listPix = []
for i in range(0, rows):
    color = redsrc[i, 20]
    listPix.append(color)

# print(listPix)

lastPix = []
lastPixT = []
lastPixD = []

for i in range(0, len(listPix) - 1):
    subPix = int(listPix[i + 1]) - int(listPix[i])
    if subPix > 58:
        print(i)
        lastPix.append(i)
        lastPixT.append(i)
    if subPix < -35:
        print(i)
        lastPix.append(i)
        lastPixD.append(i)

print(lastPix, lastPixT, lastPixD)

for i in range(len(lastPix)):
    try:
        if lastPix[i + 1] - lastPix[i] == 1:
            lastPix.remove(lastPix[i + 1])
    except IndexError:
        pass

print(lastPix)
print("24:", listPix[24], listPix[25], listPix[26])

for i in range(len(lastPix)):
    lastPix[i] = lastPix[i] + 1
    if i % 2 == 1:
        avrline = int((lastPix[i] - lastPix[i - 1]) / 2 + lastPix[i - 1])
        for j in range(cols):
            srcLine[avrline, j] = [255, 255, 0]
    for j in range(cols):
        srcLine[lastPix[i], j] = [0, 255, 0]

srcLineRed = srcLine[:, :, 2]
cv2.imshow("srcLine", srcLine)
cv2.imwrite("srcLine.jpg", srcLine)

file = open('listex.txt', 'w', encoding='utf-8')
for i in range(len(listPix)):
    file.write(str(listPix[i]) + '\r')
file.close()
cv2.waitKey()
