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

a = 0.8
b = 50
for i in range(rows):
    for j in range(cols):
        color = img[i, j] * a + b
        if color>255:
            dst[i,j]=255
        else:
            dst[i, j] = color

cv2.imshow('dst',dst)

listPix = []
for i in range(0,rows):
    color = redsrc[i,20]
    listPix.append(color)

# print(listPix)

for i in range(0,len(listPix)-1):
    subPix = int(listPix[i+1])-int(listPix[i])
    if subPix >58:
        print(i)
    if subPix < -60:
        print(i)

print("24:",listPix[24],listPix[25],listPix[26])

file = open('listex.txt', 'w', encoding='utf-8')
for i in range(len(listPix)):
    file.write(str(listPix[i])+'\r')
file.close()
cv2.waitKey()
