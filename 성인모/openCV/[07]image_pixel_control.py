import numpy as np
import cv2

img = cv2.imread('images/flower.jpg')

#픽셀값 추출
# print(img[300, 200]) # 전체
# print(img[300, 200, 0]) # 개별추츨(B)
# print(img.item(300,200,0)) #개별추출-함수활용(B)

# 개별 픽셀 변경 - 단순한 방법
# img[300,200] = [0,0,0] #전체
# img[300,200,0] = 0 #B
# img[300,200,1] = 0 #G
# img[300,200,2] = 0 #R

# 개별 픽셀 변경 - numpy 함수활용(효율적)
# img.itemset((300,200,0),100) # B
# img.itemset((300,200,1),100) # G
# img.itemset((300,200,2),100) # R

# 이미지 속성 get
# print(img.shape) #(height, width, 컬러채널수)
# print(img.size) #이미지 사이즈(총 바이트)
# print(img.dtype) #이미지 데이터타입 ex)uint8

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
