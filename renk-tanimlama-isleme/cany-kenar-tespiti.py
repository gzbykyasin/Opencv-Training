import cv2
import numpy as np
from matplotlib import pyplot as plt

kamera=cv2.VideoCapture(0)

while(1):
    ret,frame=kamera.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dusuk=np.array([100,60,60])
    yuksek=np.array([140,255,255])

    kenarlar=cv2.Canny(frame,75,100)
    """
    lap=cv2.Laplacian(frame,cv2.CV_64F)
    sobx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    soby = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    mask=cv2.inRange(hsv,dusuk,yuksek)
    son=cv2.bitwise_and(frame,frame,mask=mask)"""

    cv2.imshow('orjinal',frame)
    cv2.imshow('kenarlar',kenarlar)
    """  cv2.imshow('son',son)

cv2.imshow('lap', lap)
 cv2.imshow('sobx', sobx)
 cv2.imshow('soby', soby)"""

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()