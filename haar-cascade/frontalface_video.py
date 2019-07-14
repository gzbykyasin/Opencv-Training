import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
yuz_cascade=cv2.CascadeClassifier('haarcascade-frontalface-default.xml')

while(1):
    ret,frame=kamera.read()
    griFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuz_cascade_1 = yuz_cascade.detectMultiScale(griFrame, 1.4,4)

    for(x,y,w,h) in yuz_cascade_1:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)


    cv2.imshow('goruntu',frame)
    if cv2.waitKey(20)& 0XFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
