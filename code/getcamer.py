import numpy as np
import cv2

cap = cv2.VideoCapture(1)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
ret,frame = cap.read()

frame = frame[370:620, 385:730]
cv2.imwrite("camSave.jpg",frame)
while(cap.isOpened()):
    listPixavr = []
    ret,frame = cap.read()
    frame = frame[370:620, 385:730]
    redsrc = frame[:, :, 2]
    rows, cols, channels = frame.shape
    srcLine = frame.copy()

    dst = redsrc.copy()
    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # t, frame = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 重构建取样函数

    def getAvrPix():
        sampelLine = []
        x = 30
        color = 0
        CaiyanX = 12
        for i in range(CaiyanX):
            x = x + 15
            sampelLine.append(x)
            # print(sampelLine)

        for i in range(0, rows):
            for j in range(len(sampelLine)):
                color = color + int(dst[i, j])
            color = int(color / CaiyanX)
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
                if lastPix[i] - lastPix[i - 1] > 20:  # 前面无线
                    if lastPix[i + 1] - lastPix[i] < 5:
                        lastPix.remove(lastPix[i + 1])  # 减去i+1 这条线
                if lastPix[i] - lastPix[i - 1] < 20:
                    if lastPix[i + 1] - lastPix[i] < 5:
                        lastPix.remove(lastPix[i])  # 减去i 这条线

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
        srcLine[i, 20] = [255, 0, 0]
        srcLine[i, 40] = [255, 0, 0]
        srcLine[i, 80] = [255, 0, 0]
        srcLine[i, 100] = [255, 0, 0]
        srcLine[i, 120] = [255, 0, 0]

    cv2.imshow('frame',srcLine)
    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()