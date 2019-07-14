import cv2
import numpy as np

def kaydet(path,image,jpg_kalite=None,png_compress=None):
    if jpg_kalite:
        cv2.imwrite(path,image,[int(cv2.IMWRITE_JPEG_QUALITY),jpg_kalite])
    elif png_compress:
        cv2.imwrite(path,image,[int(cv2.IMWRITE_PNG_COMPRESSION),png_compress])
    else:
        cv2.imwrite(path,image)

def main():
    impath="cicek.jpg"
    img=cv2.imread(impath)

    cv2.imshow('cicek',img)

    cikis_png="cicek2.png"
    kaydet(cikis_png,img,png_compress=0)

    cikis_jpg="cicek3.jpg"
    kaydet(cikis_jpg,img,jpg_kalite=1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()