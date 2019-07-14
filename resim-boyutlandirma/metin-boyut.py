import cv2
import numpy as np

def  metin_yaz():
    img=np.zeros((640,720,3),dtype='uint8')
    img.fill(255)

    fontscale=1.0
    color=(0,0,255)
    fontface=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, 'Yasin GOZUBUYUK',(25,40),fontface,fontscale,color)
    cv2.putText(img, 'Yasin GOZUBUYUK', (25, 80), cv2.FONT_HERSHEY_COMPLEX_SMALL, fontscale, color)
    cv2.putText(img, 'Yasin GOZUBUYUK', (25, 120), cv2.FONT_HERSHEY_DUPLEX, fontscale, color)
    cv2.putText(img, 'Yasin GOZUBUYUK', (25, 160), cv2.FONT_HERSHEY_PLAIN, fontscale, color)
    cv2.putText(img, 'Yasin GOZUBUYUK', (25, 200), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, fontscale, color)
    cv2.putText(img, 'Yasin GOZUBUYUK', (25, 240), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontscale, color)
    cv2.putText(img, 'Yasin GOZUBUYUK', (25, 280), cv2.FONT_HERSHEY_SIMPLEX, fontscale, color)
    cv2.putText(img, 'Yasin GOZUBUYUK', (25, 320), cv2.FONT_HERSHEY_TRIPLEX, fontscale, color)
    cv2.putText(img, 'Yasin GOZUBUYUK', (25, 360), cv2.FONT_ITALIC, fontscale, color)

    cv2.namedWindow('text ornekler')
    cv2.imshow('text ornekler',img)
    cv2.imwrite('text-ornekler.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    metin_yaz()

if __name__ == '__main__':
    main()
