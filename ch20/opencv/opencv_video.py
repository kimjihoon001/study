# opencv_video.py

import cv2

# 이미지 파일 읽기
# cap = cv2.VideoCapture(0)     # 웹캠 사용
cap = cv2.VideoCapture(r'ch20\opencv\turtle.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow('Load Image', edges)
    
    # 키보드로 입력되는 키를 인식하여 정수값 반환
    if cv2.waitKey(1) == ord('q'):      # 대기 시간 (ms)
        break

    # waitKey = 1000/FPS        # 1배속 설정
    
cap.release()       # 비디오 장치 사용후 자원을 해제
cv2.destroyAllWindows()     # 모든 openCV 창 닫기