import cv2
MicaPic = cv2.imread("../img/w1.png")
cv2.imshow("Mica",MicaPic)

dst = cv2.cvtColor(MicaPic,cv2.COLOR_BGR2GRAY)
t,thd=cv2.threshold(dst,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("Micath",thd)











key = cv2.waitKey()
if key!=-1:
    print("out")