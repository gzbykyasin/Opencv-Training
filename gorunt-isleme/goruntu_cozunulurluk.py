import cv2
import numpy as np
from matplotlib import pyplot as plt

kamera=cv2.VideoCapture(0)

def cozun_1080p():
    kamera.set(3,1920)
    kamera.set(4,1080)
def cozun_720p():
    kamera.set(3,1280)
    kamera.set(4,720)
def cozun_480p():
    kamera.set(3,640)
    kamera.set(4,480)
def cozun_belirle(width,height):
    kamera.set(3,width)
    kamera.set(4,height)
    
def skalalama(goruntu,percent=75):
    width=int(goruntu.shape[1]*percent/100)
    height = int(goruntu.shape[0] * percent / 100)
    boyut=(width,height)
    return cv2.resize(goruntu,boyut,interpolation=cv2.INTER_AREA)

#cozun_720p()
w=int(input('width'))
h=int(input('height'))
cozun_belirle(w,h)
while True:
    ret , goruntu=kamera.read()
    frame60=skalalama(goruntu,60)
    frame30 = skalalama(goruntu, 30)
    if ret==True:
        cv2.imshow('Video Goruntu1',frame60)
        cv2.imshow('Video Goruntu2', frame30)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()