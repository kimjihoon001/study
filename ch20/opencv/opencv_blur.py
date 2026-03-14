# opencv_blur.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\sample.jpg')

blured = cv2.GaussianBlur(image, (31,31), 0)

# 블러 함수에서 커널 크기는 홀수
# 홀수 크기 커널이어야 중앙 픽셀이 존재하여 대칭적 처리가능
# 픽셀 주변 값 평균/기중평균 등으로 처리


# 이미지 창에 표시
cv2.imshow('Gaussian Image', blured)
cv2.waitKey(0)      # 0 : 무한대기
cv2.destroyAllWindows()

# 가우시안 = 가우스(Gauss)가 연구한 수학적 분포 또는 함수