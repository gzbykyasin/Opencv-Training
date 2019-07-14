import cv2
import numpy as np
from matplotlib import pyplot as plt

kamera=cv2.VideoCapture(0)
kamera.set(3,640)
kamera.set(4,320)
while(1):
    ret,frame=kamera.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dusuk=np.array([30,40,90],np.float32)
    yuksek=np.array([240,200,150],np.float32)


    mask=cv2.inRange(hsv,dusuk,yuksek)
    son=cv2.bitwise_and(frame,frame,mask=mask)

    kernel = np.ones((3, 3), np.float32)/9
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel,iterations=1)
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('orjinal',frame)
    cv2.imshow('son hali',son)
    cv2.imwrite('deneme.png',dilation)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()