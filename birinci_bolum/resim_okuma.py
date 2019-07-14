import cv2
import numpy as np
resim=cv2.imread('cicek.jpg',0)         #dosya okumaya yarıyor yolu gösteriyoruz. 0 yazarsak gri tonda çağırmış  oluyoruz
cv2.imshow('resim-gosteriyoruz',resim)  #resim gösterme yani window oluşturma ve  title belirleme
cv2.imwrite('gri.jpg',resim)            #resmi başka bir uzantıda kaydetme


cv2.waitKey(0)                          #herhangi bir tuşa basıldıktan sonra kapat (mesela 100 yaptığımızda 100 saniye bekle ve kapat)
cv2.destroyAllWindows()                 #diğer tüm pencereleri yok et diyor

