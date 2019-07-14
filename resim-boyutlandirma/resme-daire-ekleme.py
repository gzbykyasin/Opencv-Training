import cv2
import numpy as np
from matplotlib import pyplot as plt

resim=np.zeros((400,400,3),dtype='uint8')

cv2.line(resim,(10,10),(390,210),(0,255,0),3)
cv2.line(resim,(10,210),(390,10),(0,255,0),3)
cv2.line(resim,(10,10),(10,210),(0,255,0),3)
cv2.line(resim,(390,10),(390,210),(0,255,0),3)
cv2.line(resim,(300,60),(300,160),(0,255,0),3)
cv2.line(resim,(100,60),(100,160),(0,255,0),3)
cv2.line(resim,(10,110),(390,110),(0,255,0),3)
cv2.line(resim,(10,10),(390,10),(0,255,0),3)
cv2.line(resim,(10,210),(390,210),(0,255,0),3)


cv2.circle(resim,(200,350),20,(0,0,255),3)
cv2.imshow('siyah',resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
