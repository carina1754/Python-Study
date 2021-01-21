import cv2
import numpy as np


# 단순 더하기
# def addImage(image1, image2):
#     img1 = cv2.imread(image1)
#     img2 = cv2.imread(image2)
#
#     cv2.imshow('img1', img1)
#     cv2.imshow('img2', img2)
#
#     add_Image1 = img1 + img2
#     add_Image2 = cv2.add(img1, img2)
#
#     cv2.imshow('img1+img2', add_Image1)
#     cv2.imshow('add(img1, img2)', add_Image2)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#
# addImage('images/flower.jpg', 'images/flower2.jpg')


# 블렌딩
def onMouse(x):
    pass


def imgBlending(image1, image2):
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    cv2.namedWindow('imgPane')
    cv2.createTrackbar('Mixing', 'imgPane', 0, 100, onMouse)
    mix = cv2.getTrackbarPos('Mixing', 'imgPane')

    while True:
        img = cv2.addWeighted(img1, float(100 - mix)/100, img2, float(mix) / 100, 0)
        cv2.imshow('imgPane', img)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        mix = cv2.getTrackbarPos('Mixing', 'imgPane')

    cv2.destroyAllWindows()


imgBlending('images/flower.jpg', 'images/flower2.jpg')
