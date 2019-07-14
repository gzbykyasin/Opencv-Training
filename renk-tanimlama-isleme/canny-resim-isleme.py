import cv2
import numpy as np
from matplotlib import pyplot as plt

resim=cv2.imread('cicek.jpg',0)

row,col=resim.shape

kenarlar=cv2.Canny(resim,100,200)
print("{} \t {} \t".format(row,col))

plt.subplot(121),plt.imshow(resim,cmap='gray')
plt.title('orjinal'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(kenarlar,cmap='gray')
plt.title('kenarlar'),plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()