import cv2
import numpy as np
from matplotlib import pyplot as plt

kamera=cv2.VideoCapture('smile.mp4')

while(1):
    ret,frame=kamera.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dusuk_kirmizi=np.array([0,100,50])
    ust_kirmizi=np.array([30,255,255])
    mask=cv2.inRange(hsv,dusuk_kirmizi,ust_kirmizi)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)


    cv2.imshow('orjinal',frame)
    cv2.imshow('mask', mask)
    cv2.imshow('son hali', son_resim)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()