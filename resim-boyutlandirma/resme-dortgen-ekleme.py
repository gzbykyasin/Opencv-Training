import cv2
import numpy as np
from matplotlib import pyplot as plt

resim=np.zeros((400,400,3),dtype='uint8')

#cv2.imread('cicek.jpg')
cv2.rectangle(resim,(0,0),(50,50),(255,0,0),3)
cv2.imshow('cicek',resim)
cv2.rectangle(resim,(200,50),(300,150),(255,0,0),2)
cv2.imshow('cicek2',resim)

cv2.waitKey(0)
cv2.destroyAllWindows()