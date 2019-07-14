import cv2
from matplotlib import pyplot as plt
import numpy as np

img1=cv2.imread('cicek.jpg')
img2=cv2.imread('cicek-gri.png')

toplam1=cv2.add(img1,img2)                          #iki resmi topladık
toplam2=cv2.addWeighted(img1,0.7,img2,0.3,0)        #iki resmi topladık ve ağırlık oranlarını belirledik

cv2.imshow('toplanmıs-resim1',toplam1)
cv2.imshow('toplanmıs-resim2',toplam2)

cv2.waitKey(0)
cv2.destroyAllWindows()