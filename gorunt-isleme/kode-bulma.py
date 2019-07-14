import cv2
from matplotlib import pyplot as plt
import numpy as np

resim=cv2.imread('kose-bulma.jpg')
griton=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

griton=np.float32(griton)

koseler=cv2.goodFeaturesToTrack(griton,100,0.1,50)
koseler=np.int0(koseler)

for kose in koseler:
    x,y=kose.ravel()
    cv2.circle(resim,(x,y),3,255,-1)
    print("------x-------")
    print(x)
    print("------y-------")
    print(y)
cv2.imshow('koseler',resim)
cv2.imshow('griton',griton)
print(koseler)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.destroyAllWindows()