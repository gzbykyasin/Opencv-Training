import cv2
import numpy as np

img = cv2.imread('cicek.jpg')
print(str(img.shape))               #yükseklik genişlik ve renk sayısı(mesele sarı yeşil ve kırmızı renk varsa 3 gösteriyor)
print(str(img.item(100,100,1)))     #ilgili pikseldeki (genislik ve yükseklik) 0 ise mavi 1 ise sarı 2 ise kırmızı renk oranını görüyoruz
print(str(img.size))                #piksel sayısını veriyor
ROI=img[210:310,360:460]            #ilki y ikincisi x eksenindeki kesilecek olan parçayı belirtmeye yarıyor
cv2.imshow('roi',ROI)               #bu kesilen parçayı farklı bir windowda gösteriyoruz
print(img.dtype)                    #veri tipini görüntülüyoruz
img[210:310,260:360]=ROI            #buradaki kesilen parçanın y eksenindeki koordinatlarını değiştirip resimde gösterdik yani işledik
for i in range(50,400):             #burada 50 ye 50 den başlayarak resmi çizmeye başlıyoruz. tam bir kare yapıyoruz. boyutları 350x350
    img.itemset((50, i, 2), 255)
    img.itemset((i,50,2),255)
    img.itemset((400,i,2),255)
    img.itemset((i, 400, 2), 255)
b,g,r=cv2.split(img)               #renk sayısını b,g,r olarak kaydediyor. Bilgisayarı çok kastığı için pek tercih etmiyoruz
img=cv2.merge((b*2,g*2,r*2))       #burada renk sayılarını 2 ile çarpıp img değişkenine kaydediyoruz ve ekranda değişik bir resim çıkmmış oluyor :D
img[:,:,0]=255                     #bu şekilde renk bileşenine erişmek daha kolay ve bilgisayarı daha az yoruyor


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
