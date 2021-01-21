import cv2
import numpy


def bitOperation(hpos, vpos):
    img1 = cv2.imread('images/flower.jpg')
    img2 = cv2.imread('images/logo.jpg')

    # 로고 배치영역
    rows, cols, channels = img2.shape
    roi = img1[vpos:rows + vpos, hpos:cols + hpos]

    # 로고 마스크,역마스크
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2_gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # ROI중 로고만 검정색으로
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # 로고이미지에서 로고 추출
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    # 로고이미지 배경을 투명으로, 이후 ROI에 로고 삽입
    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos:rows + vpos, hpos:cols + hpos] = dst

    cv2.imshow('result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


bitOperation(10, 10)
