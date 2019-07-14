import cv2
import numpy as np
from matplotlib import pyplot as plt





def main():

    impath="cicek.jpg"
    img=cv2.imread(impath)
    upgrade = cv2.pyrUp(img)
    downable=cv2.pyrDown(img)

    cv2.imshow('orjinal',img)
    cv2.imshow('alt-seviye', downable)
    cv2.imshow('ust-seviye',  upgrade)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()