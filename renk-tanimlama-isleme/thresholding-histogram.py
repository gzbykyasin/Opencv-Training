import cv2
import numpy as np
from matplotlib import pyplot as plt

resim=cv2.imread('gurultuluresim.JPG',0)

_,thresh1=cv2.threshold(resim,125,255,cv2.THRESH_BINARY)
_,thresh2=cv2.threshold(resim,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur=cv2.GaussianBlur(resim,(5,5),0)
_,thresh3=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

resimler=[  resim,0,thresh1,
            resim,0,thresh2,
            blur,0,thresh3  ]

basliklar=['orjinal','histogram','thresh1',
           'orjinal','histogram','threash2',
           'blur','histogram','thresh3' ]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(resimler[i*3],cmap='gray')
    plt.title(basliklar[i*3]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(resimler[i*3].ravel(),256)
    plt.title(basliklar[i*3+1]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(resimler[i*3+2],cmap='gray')
    plt.title(basliklar[i*3+2]),plt.xticks([]),plt.yticks([])

plt.show()