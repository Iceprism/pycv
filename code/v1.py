import cv2
import numpy as np
import matplotlib.pyplot as plt
MicaPic = cv2.imread("../img/w1.png")
plt.figure("res")
plt.subplot(121)
plt.imshow(MicaPic)

cv2.imshow("Mica",MicaPic)
k=np.ones((5,5),np.uint8)

dst1 = cv2.cvtColor(MicaPic,cv2.COLOR_RGB2GRAY)
plt.subplot(122)
plt.imshow(dst1,cmap=plt.cm.gray)

t,thd=cv2.threshold(dst1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

thd=cv2.morphologyEx(thd,cv2.MORPH_CLOSE,k,iterations=2)

cv2.imshow("Micath",thd)
src = MicaPic
# thd = cv2.bitwise_not(thd)
image,contours,hierarchy = cv2.findContours(thd,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
src=cv2.drawContours(src,contours,-1,(0,255,0),2)


cv2.imshow("result",src)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
