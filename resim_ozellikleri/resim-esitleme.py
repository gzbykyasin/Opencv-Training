import numpy as np
import  cv2
from matplotlib import pyplot as plt

resim_aranacak=cv2.imread("kucuk-resim.JPG",0)

resim_orjinal=cv2.imread("buyuk-resim.JPG",0)

orb=cv2.ORB_create()
an1,hdf1=orb.detectAndCompute(resim_aranacak,None)
an2,hdf2=orb.detectAndCompute(resim_orjinal,None)

bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
eslesmeler=bf.match(hdf1,hdf2)
print("eslesmeler")
print(eslesmeler)
eslesmeler=sorted(eslesmeler,key=lambda x:x.distance)
print("eslesmeler yeni")
print(eslesmeler)
son_resim=cv2.drawMatches(resim_aranacak,an1,resim_orjinal,an2,eslesmeler[:10],None,flags=2)
plt.imshow(son_resim)
plt.show()