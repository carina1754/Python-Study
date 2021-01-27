import cv2
import numpy as np


# BGR>HSV 전환
# def hsv():
#     blue = np.uint8([[[255, 0, 0]]])
#     green = np.uint8([[[0, 255, 0]]])
#     red = np.uint8([[[0, 0, 255]]])
#
#     hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
#     hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
#     hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
#
#     print('HSV_BLUE', hsv_blue)
#     print('HSV_GREEN', hsv_green)
#     print('HSV_RED', hsv_red)
#

def color_picking():
    try:
        print('카메라 구동')
        cap = cv2.VideoCapture(1)
    except:
        print('카메라 구동실패')
        return

    while True:
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 추출색상 범위 가정
        lower_blue = np.array([110, 100, 100])
        upper_blue = np.array([130, 255, 255])

        lower_green = np.array([50, 100, 100])
        upper_green = np.array([70, 255, 255])

        lower_red = np.array([-10, 100, 100])
        upper_red = np.array([10, 255, 255])

        # 추출 임계값 설정
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_red = cv2.inRange(hsv, lower_red, upper_red)

        # mask 비트연산
        blue_cam = cv2.bitwise_and(frame, frame, mask=mask_blue)
        green_cam = cv2.bitwise_and(frame, frame, mask=mask_green)
        red_cam = cv2.bitwise_and(frame, frame, mask=mask_red)

        cv2.imshow('original', frame)
        cv2.imshow('blue', blue_cam)
        cv2.imshow('green', green_cam)
        cv2.imshow('red', red_cam)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()


color_picking()
