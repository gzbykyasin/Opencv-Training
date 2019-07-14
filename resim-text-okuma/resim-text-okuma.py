from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import Image
import pytesseract as pyt

pyt.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"


def metin_oku(img_yolu):
    img=cv2.imread(img_yolu)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    kernel=np.ones((1,1),np.uint8)
    img=cv2.erode(img,kernel,iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)
    img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,43,3)
    cv2.imwrite('gurultusuz.jpg',img)

    sonuc=pyt.image_to_string(Image.open('gurultusuz.jpg'))
    return sonuc

print("--------------------------------")
print("Metin Okuma")
print("--------------------------------")
print(metin_oku("sudoku.jpg"))
print("--------------------------------")
print("Başarılı")