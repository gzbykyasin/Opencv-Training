import cv2
import numpy as np
from matplotlib import pyplot as plt

resim=cv2.imread('sayfa.jpg')

_,th1=cv2.threshold(resim,12,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(resim,12,255,cv2.THRESH_BINARY_INV)
blur=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
_,th3=cv2.threshold(blur,12,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
_,th4=cv2.threshold(blur,12,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
gaus1=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,39,3)
mean2=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,43,3)
resimler=[resim,th1,th2,gaus1,
          resim,th3,th4,mean2]
basliklar=['orjinal','thresh1','thresh2','gaus1',
           'orjinal','thresh3','thresh4','mean2']

for i in range(2):
    plt.subplot(2,4,i*4+1),plt.imshow(resimler[i*4],cmap='gray')
    plt.title(basliklar[i*4]),plt.yticks([]),plt.xticks([])
    plt.subplot(2, 4, i * 4 + 2), plt.imshow(resimler[i * 4 + 1], cmap='gray')
    plt.title(basliklar[i * 4 + 1]), plt.yticks([]), plt.xticks([])
    plt.subplot(2,4,i*4+3),plt.imshow(resimler[i*4+2],cmap='gray')
    plt.title(basliklar[i*4+2]),plt.yticks([]),plt.xticks([])
    plt.subplot(2, 4, i * 4 + 4), plt.imshow(resimler[i * 4 + 3], cmap='gray')
    plt.title(basliklar[i * 4 + 3]), plt.yticks([]), plt.xticks([])

plt.show()
cv2.imshow('gauss',gaus1)


cv2.waitKey(0)
cv2.destroyAllWindows()
