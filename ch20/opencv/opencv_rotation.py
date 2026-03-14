# opencv_rotation.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\sample.jpg')

# print(image.shape)
(h,w) = image.shape[0:2]

center = (w//2, h//2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
# 이미지 창에 표시
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)      # 0 : 무한대기
cv2.destroyAllWindows()