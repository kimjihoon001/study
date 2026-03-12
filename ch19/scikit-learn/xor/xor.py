# xor.py

# import sklearn as sk
from sklearn import svm 
from sklearn import metrics

# 1. 데이터 수집 및 전처리

# 2. 알고리즘 선택
clf = svm.SVC()

# 3. 학습/훈련 => 모델 생성
# fit(학습데이터, 학습레이블)
clf.fit(
    [
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ], 
    [0,1,1,0]
)

# 4. 예측
pre = clf.predict(
    [[0,1],[1,1]]
)

print(pre)

# 5. 정확도 평가
ac_score = metrics.accuracy_score([1,0], pre)

print(f'정답률ㅣ {ac_score}')
