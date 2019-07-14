import cv2
import numpy as np
from matplotlib import pyplot as plt

kamera=cv2.VideoCapture(1)

fourcc=cv2.VideoWriter_fourcc(*'XVID')

kayit=cv2.VideoWriter('kayit.avi',fourcc,30.0,(640,480))


while (kamera.isOpened()):
    ret,video=kamera.read()
    if ret==True:
        video=cv2.flip(video,0)
        kayit.write(video)
        cv2.imshow('video',video)
    if cv2.waitKey(20)& 0xFF==ord('q'):
        break

kamera.release()
kayit.release()
cv2.destroyAllWindows()
