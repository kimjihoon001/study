# xor_train2.py

from sklearn import svm         # 알고리즘 모듈
from sklearn import metrics     # 행렬, 정확도 관련 모듈
import pandas as pd

# 1. 데이터 수집 및 전처리
xor_data = [
    # P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [0, 0, 0]
]
# 데이터 가공 => 학습 데이터와 레이블 분리
xor_df = pd.DataFrame(xor_data)

# 학습 데이터(독립변수)
data = xor_df.loc[:,0:1]
# 학습 레이블(종속변수)
label = xor_df.loc[:,2]

print(data)
print(label)

# # 2. 알고리즘 선택
clf = svm.SVC()

# # 3. 학습/훈련 => 모델 생성
# # fit(학습데이터, 학습레이블)
clf.fit(data,label)


# # 4. 예측
pre = clf.predict(data)
print(pre)

# # 5. 정확도 평가
ac_score = metrics.accuracy_score(label, pre)

print(f'정답률ㅣ {ac_score}')

