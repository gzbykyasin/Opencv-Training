from matplotlib import pyplot as plt
import cv2
import numpy as np

resim=cv2.imread('buyuk-resim.JPG')

resim_gray=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

nesne=cv2.imread('kucuk-resim.JPG',0)

w,h=nesne.shape[::-1]

res=cv2.matchTemplate(resim_gray,nesne,cv2.TM_CCOEFF_NORMED)
threshold=0.80
log=np.where(res>threshold)

for lg in zip(*log[::-1]):
    cv2.rectangle(resim,lg,(lg[0]+w,lg[1]+h),(0,255,255),1)

cv2.imshow('bulunan nesneler',resim)
cv2.waitKey(0)
cv2.destroyAllWindows()