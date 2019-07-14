import cv2
from matplotlib import pyplot as plt
import numpy as np


resim=np.zeros((400,400,3),dtype='uint8')

cv2.rectangle(resim,(10,10),(390,210),(0,0,255),3)
cv2.circle(resim,(200,110),90,(255,0,0),3)
cv2.putText(resim,'Yasin G.',(50,125),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(0,255,0),3,cv2.LINE_4)
cv2.imshow('resim',resim)

cv2.waitKey(0)

cv2.destroyAllWindows()