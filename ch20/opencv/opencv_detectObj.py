# opencv_detectObj.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\people.jpg')

# 2. 얼굴 검출을 위한 모델 확인
# haarcascade_eye.xml
# haarcascade_russian_plate_number.xml
# haarcascade_car.xml

face_path = cv2.data.haarcascades + \
        'haarcascade_frontalface_default.xml'

# 3. 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 4. 캐드케이스 분류기 생성
face_cascade = cv2.CascadeClassifier(face_path)

faces = face_cascade.detectMultiScale(
    gray,                       # 입력 이미지(그레이스케일)
    scaleFactor=1.1,            # 이미지 크기를 줄여가며 검출(1.1배씩 감소:10%씩 줄여가면서 검사)
                                # 얼굴 크기는 사람마다 다르므로 이미지를 축소하면서 얼굴을 검색
    minNeighbors=3,             # 객체로 인지되기 위한 최소 중복 검출수
                                # 보통 4~6 정도가 안정적
    minSize=(10,10),            # 최소 객체(얼굴) 크기 => 이 크기보다 작은 객체는 얼굴로 간주 않음
    maxSize=(200,600)           # 최대 객체(얼굴) 크기 => 이 크기보다 큰 객체는 얼굴로 간주 않음
    )


print(faces)        # [x, y, w, h]

for (x, y, w,h) in faces:
    cv2.rectangle(image,
                (x,y),
                (x+w,y+h),
                (200, 0, 0),
                2                
                )

# 이미지 창에 표시
cv2.imshow('Face Detection', image)
cv2.waitKey(0)      # 0 : 무한대기
cv2.destroyAllWindows()