# opencv_resizepy
import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\sample.jpg')

resized = cv2.resize(image, (300,300))        # 단위: 픽셀(pixel)

# 이미지 창에 표시
cv2.imshow('Resized Image', resized)
cv2.waitKey(0)      # 0 : 무한대기
cv2.destroyAllWindows()