import cv2
import numpy as np
from matplotlib import pyplot as plt

kamera=cv2.VideoCapture('smile.mp4')
kamera.set(cv2.CAP_PROP_FRAME_WIDTH,640.0)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,480.0)

while True:
    ret, goruntu = kamera.read()
    gri_ton=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    print('Size:\t'+str(kamera.get(3))+" x "+str(kamera.get(4)))
    cv2.imshow('video',goruntu)
    cv2.imshow('gri video', gri_ton)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()