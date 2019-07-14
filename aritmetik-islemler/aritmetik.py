import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('cicek.jpg')
print(img[80,80])                   #b g r değerlerini görüyoruz
img[80,80]=[255,255,255]            #80 x 80 deki pikselin rengini değiştirme komutu

bolge=img[100:150,200:250]          #bolge seçme komutu
img[50:100,200:250]=bolge           #bolgeyi resim üzerinde biryere kopyalıyoruz
bolge[:,:,0]=255                    #bolgenin renklerini değiştir
bolge[:,:,1]=255
bolge[:,:,2]=255
                                    #aşağıda bolgeye dış kenarlık ekliyoruz y2-y2 ve x2-x1 şeklinde daha sonra renk  ve kalınlık değerleri
cv2.rectangle(img,(200,100),(250,150),(0,255,255),4)
cv2.imshow('cicek',img)
cv2.imshow('bolge',bolge)

cv2.waitKey(0)
cv2.destroyAllWindows()