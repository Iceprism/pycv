#coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
import serial
import time

serialPort="COM5"
baudRate=115200
ser=serial.Serial(serialPort, baudRate, timeout=1)
time.sleep(1)

MicaPic = cv2.imread("../img/w1.png")
croppedsrc = MicaPic[371:463, 0:512]
cv2.imshow('cr',croppedsrc)
cv2.imwrite("cutsrc.jpg",croppedsrc)
plt.figure("res")
plt.subplot(121)
plt.imshow(MicaPic)

cv2.imshow("Mica",MicaPic)
k=np.ones((3,3),np.uint8)

dst1 = cv2.cvtColor(MicaPic,cv2.COLOR_RGB2GRAY)



plt.subplot(122)
plt.imshow(dst1,cmap=plt.cm.gray)

t,thd=cv2.threshold(dst1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
thd=cv2.morphologyEx(thd,cv2.MORPH_CLOSE,k,iterations=3)
cv2.imshow("thd",thd)
thd = cv2.bitwise_not(thd)


img = thd
print(np.shape(img))
Laplacian = cv2.Laplacian(img,cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)

_, labels, stats, centroids = cv2.connectedComponentsWithStats(Laplacian)
print(centroids)
print("123")
print("stats = ", stats)
i = 0
for istat in stats:
    if istat[4] < 100:
        # print(i)
        print(istat[0:2])
        if istat[3] > istat[4]:
            r = istat[3]
        else:
            r = istat[4]
        cv2.rectangle(Laplacian, tuple(istat[0:2]), tuple(istat[0:2] + istat[2:4]), (0, 0, 255), thickness=-1)
    i = i + 1


cv2.imshow("img1",Laplacian)
cv2.imwrite("轮廓.jpg",Laplacian)
cropped = Laplacian[371:463, 0:512]
cv2.imshow("cut",cropped)
cropped_C = cv2.bitwise_not(cropped)
Sobely = cv2.Sobel(cropped_C,cv2.CV_64F,0,1)
q = 0
global tp
tp = 0
ti = 0
nottox = 0
nottox_p = 0
for i in range(0,90):
    print(Sobely[i, 0])
    if nottox == 0:
        nottox_p = nottox_p + 1
    if Sobely[i,0] > 0:
        nottox = 2
        q = q + 1
        if tp == 0:
            tp=1
    if tp == 1:
        ss=Sobely[i, 0]
        ti = ti +1
        if Sobely[i,0] < 0:

            tp = 2
if Sobely[39,0] < 0:
    print("Y")
Sobely = cv2.convertScaleAbs(Sobely)
ti_r = int(ti/2)+nottox_p
for i in range(0,100):
    Sobely[ti_r,i] = 255


print(q)
cv2.imshow("y",Sobely)


cv2.imshow("Micath",thd)
src = MicaPic

# image,contours,hierarchy = cv2.findContours(thd,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# src=cv2.drawContours(src,contours,-1,(0,255,0),2)
xl = int(371+ti/2)+nottox_p
ptStart = (0, xl)
ptEnd = (512, xl)
point_color = (255, 255, 255) # BGR
thickness = 1
lineType = 4
cv2.line(src, ptStart, ptEnd, point_color, thickness, lineType)\


# input_s = 'a'
# input_s = (input_s + '\r\n').encode('utf-8')
# result=ser.write(input_s)
# time.sleep(2)
input_s = 'cirl180'
input_s = (input_s + '\r\n').encode('utf-8')
result=ser.write(input_s)
time.sleep(2)
ser.close()#关闭串口
print("go")


cv2.imshow("result",src)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
