import cv2
import numpy as np
from matplotlib import pyplot as plt
mavi=[255,0,0]
img=cv2.imread('cicek.jpg')

#aşağıdaki kodlar çerçeveleme için gerekli kodlardır. sağ sol üst alttan kaç piksellik bir kenarlık olacak ve kenarlıkların şekilleri ile beraber renklerini de seçebiliyoruz
replicate=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflecte=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflecte101=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT101)
wrap=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=mavi)

#tek bir çizimde tüm resimleri göstermek için aşağıdaki komutları kullanıyoruz. matplatlib kütüphanesinin bize sağladığı avantajlardan küçük bir örnek
plt.subplot(231),plt.imshow(img,'gray'),plt.title('original')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflecte,'gray'),plt.title('reflecte')
plt.subplot(234),plt.imshow(reflecte101,'gray'),plt.title('reflecte101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()