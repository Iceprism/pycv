import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
ret,frame = cap.read()
# frame = frame[370:620, 385:730]
cv2.imwrite("camSave.jpg",frame)
while(cap.isOpened()):
    ret,frame = cap.read()
    frame = frame[370:620, 385:730]
    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # t, frame = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow('frame',frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()