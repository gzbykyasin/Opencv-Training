import cv2
import numpy as np
from matplotlib import pyplot as plt

kamera=cv2.VideoCapture('video.mp4')

while(1):
    ret,frame=kamera.read()


    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dusuk=np.array([100,60,60])
    yuksek=np.array([140,255,255])
    #print(cv2.__version__) opencv version öğrenme
    mask=cv2.inRange(frame,dusuk,yuksek)
    son=cv2.bitwise_and(frame,frame,mask=mask)
    kernel=np.ones((15,15),np.float32)/225
    smt=cv2.filter2D(son,-1,kernel)
    mdn=cv2.medianBlur(son,15)
    blr=cv2.GaussianBlur(son,(15,15),0)
    blt=cv2.bilateralFilter(son,15,75,75)

    cv2.imshow('orjinal',frame)
    cv2.imshow('smt',smt)
    cv2.imshow('blr', blr)
    cv2.imshow('mdn', mdn)
    cv2.imshow('blt', blt)
    cv2.imshow('son',son)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()