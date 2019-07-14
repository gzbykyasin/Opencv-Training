import cv2
import numpy as np

img1=cv2.imread('yuz.jpg')
img2=cv2.imread('yuz2.png')
img3=cv2.imread('yuz3.jpg')
img4=cv2.imread('kalabalik.jpg')
img5=cv2.imread('kalabalik2.jpg')

yuz_cas=cv2.CascadeClassifier('haarcascade-frontalface-default.xml')

gri_img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gri_img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gri_img3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
gri_img4=cv2.cvtColor(img4,cv2.COLOR_BGR2GRAY)
gri_img5=cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)

yuzler1=yuz_cas.detectMultiScale(gri_img1,1.1,4)
yuzler2=yuz_cas.detectMultiScale(gri_img2,1.1,4)
yuzler3=yuz_cas.detectMultiScale(gri_img3,1.1,4)
yuzler4=yuz_cas.detectMultiScale(gri_img4,1.1,4)
yuzler5=yuz_cas.detectMultiScale(gri_img5,1.1,4)
c=0
d=0
e=0
f=0
g=0
for (x,y,w,h) in yuzler1:
    c=c+1
    cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow('yuz1',img1)
for (x,y,w,h) in yuzler2:
    d = d + 1
    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow('yuz2',img2)
for (x, y, w, h) in yuzler3:
    e = e + 1
    cv2.rectangle(img3, (x, y), (x + w, y + h), (0, 0, 255), 3)
    cv2.imshow('yuz3', img3)
for (x, y, w, h) in yuzler4:
    f = f + 1
    cv2.rectangle(img4, (x, y), (x + w, y + h), (0, 0, 255), 3)
    cv2.imshow('yuz4', img4)
for (x, y, w, h) in yuzler5:
    g = g + 1
    cv2.rectangle(img5, (x, y), (x + w, y + h), (0, 0, 255), 3)
    cv2.imshow('yuz5', img5)
print("yuzler{}".format(c))
print("yuzler{}".format(d))
print("yuzler{}".format(e))
print("yuzler{}".format(f))
print("yuzler{}".format(g))

cv2.waitKey(0)
cv2.destroyAllWindows()