import cv2
# import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('TkAgg')
img = cv2.imread('../img/w1.png')
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure("res")
plt.subplot(121)
plt.imshow(img),plt.axis('off')
plt.subplot(122)
plt.imshow(imgRGB),plt.axis('off')
plt.show()
