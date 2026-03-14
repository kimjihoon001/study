# opencv_DetectEdge.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\sample.jpg')

gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,
          threshold1=50,
          threshold2=100)

# 이미지 창에 표시
cv2.imshow('Edge detected Image', edges)
cv2.waitKey(0)      # 0 : 무한대기
cv2.destroyAllWindows()