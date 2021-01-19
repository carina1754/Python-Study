import cv2
import numpy as np
import matplotlib.pyplot as plt


def showImage():
    imgfile = 'images/flower.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    cv2.namedWindow('flower', cv2.WINDOW_NORMAL)
    cv2.imshow('flower', img)
    cv2.waitKey(0)
    cv2.destroyWindow()


def imgCopy():
    imgfile = 'images/flower.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    cv2.imshow('flower', img)

    k = cv2.waitKey(0) & 0xFF

    if k == 27:
        cv2.destroyWindow()
    elif k == ord('c'):
        cv2.imwrite('images/flower_copy.jpg', img)
        cv2.destroyWindow()


def showImagePlt():
    imgfile = 'images/flower.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([])
    plt.xticks([])
    plt.title('flower')
    plt.show()


# showImage()
# imgCopy()
showImagePlt()