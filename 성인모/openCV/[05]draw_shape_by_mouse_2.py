import numpy as np
import cv2
from random import shuffle
import math

mode = True
drawing = True
ix, iy = -1, -1
b = [i for i in range(256)]
g = [i for i in range(256)]
r = [i for i in range(256)]


def onMouse(event, x, y, flags, param):
    global ix, iy, drawing, mode, b, r, g

    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 누를때
        drawing = True
        ix, iy = x, y
        shuffle(b), shuffle(g), shuffle(r)

    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 움직임
        if drawing:  # L클릭 상태로 무브시
            if mode:
                cv2.rectangle(param, (ix, iy), (x, y), (b[0], g[0], r[0]), -1)
            else:
                radius = (ix - x) ** 2 + (iy - y) ** 2
                radius = int(math.sqrt(radius))
                cv2.circle(param, (ix, iy), radius, (b[0], g[0], r[0]), -1)

    elif event == cv2.EVENT_LBUTTONUP:  # 마우스 뗄때
        drawing = False



def mouseBrush():
    global mode

    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('paint')
    cv2.setMouseCallback('paint', onMouse, param=img)

    while True:
        cv2.imshow('paint', img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break
        elif k == ord('m'):
            mode = not mode

    cv2.destroyAllWindows()


mouseBrush()
