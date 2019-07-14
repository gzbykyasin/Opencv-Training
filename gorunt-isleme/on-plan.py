from matplotlib import pyplot as plt
import cv2
import numpy as np

resim=cv2.imread('on-plan.jpg')

#gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
mask=np.zeros(resim.shape[:2],np.uint8)
bgModel=np.zeros((1,65),np.float64)
fgModel=np.zeros((1,65),np.float64)

dik=(250,125,150,250)

cv2.grabCut(resim,mask,dik,bgModel,fgModel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
resim=resim*mask2[:,:,np.newaxis]

plt.imshow(resim)
plt.colorbar()
plt.show()