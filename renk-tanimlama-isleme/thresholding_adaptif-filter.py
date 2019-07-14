import cv2
import numpy as np
from matplotlib import pyplot as plt

"""resim=cv2.imread('sudoku.JPG',0)
   resim=cv2.medianBlur(resim,5)
"""
resim=cv2.imread('gurultuluresim.JPG',0)

_,thres1=cv2.threshold(resim,120,255,cv2.THRESH_BINARY)
_,thres2=cv2.threshold(resim,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

th2=cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,2)
th3=cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,2)
blur=cv2.GaussianBlur(resim,(5,5),0)
_,thres3=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
basliklar=['orjinal','basit thresh','otsu thresh','gaussian','mean','blur','thres3']
resimler=[resim,thres1,thres2,th2,th3,blur,thres3]

for i in range(7):
    plt.subplot(3,3,i+1),plt.imshow(resimler[i],cmap='gray')
    plt.title(basliklar[i]),plt.xticks([]),plt.yticks([])

plt.show()
