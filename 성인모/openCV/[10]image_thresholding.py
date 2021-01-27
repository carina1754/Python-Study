import cv2
import numpy as np



# 이미지 전역 적용
# img = cv2.imread('images/flower.jpg', cv2.IMREAD_GRAYSCALE)

# ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
#
# cv2.imshow('origin', img)
# cv2.imshow('BINARY', thr1)
# cv2.imshow('BINARY_INV', thr2)
# cv2.imshow('TRUNC', thr3)
# cv2.imshow('TOZERO', thr4)
# cv2.imshow('TOZERO_INV', thr5)

# 적응형
img = cv2.imread('images/sample.jpg', cv2.IMREAD_GRAYSCALE)

ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thr2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thr3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

title = ['origin', 'global', 'adaptive mean', 'adaptive gaussian']
images = [img,thr1,thr2,thr3]

for i in range(4):
    cv2.imshow(title[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
