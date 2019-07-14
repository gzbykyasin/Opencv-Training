import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('resim.jpg')
img2=cv2.imread('opencv.jpg')

row,col,chn=img2.shape                                      #resmin satır sütün ve kanal bilgisini aldık
roi=img1[0:row,0:col]                                       #birinci resimde ikinci resimdeki yerleştireceğimiz alanı tespit ettik

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)              #ikinci resmi gri skalaya çevirdik
cv2.imshow('gri',img2gray)
ret,mask=cv2.threshold(img2gray,20,255,cv2.THRESH_BINARY)    #resimdeki 100,255 arası renkleri kararttık kalanlar beyaz oldu
mask_inv=cv2.bitwise_not(mask)                              #burada yukarıdaki yapılan işlemin tam tersi yapılıyor
cv2.imshow('mask',mask)

cv2.imshow('tersmask',mask_inv)

im1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)               #birinci resme ikinci resimde işleyip arka planını gösterdiğimiz maskelemenin tersini ekliyoruz
cv2.imshow('img1bg',im1_bg)

im2_fg=cv2.bitwise_and(img2,img2,mask=mask)                 #ikinci resme maskelenmiş olan şeklini ekliyoruz
cv2.imshow('im2fg',im2_fg)

ended_picture=cv2.add(im1_bg,im2_fg)                        #iki resmin ilgili yerlerini topluyoruz
img1[0:row,0:col]=ended_picture                             #bu alanı tüm resme ekliyoruz
cv2.imshow('sonresim',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()