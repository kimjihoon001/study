# stats1.py

import statsmodels.api as sm

# data = sm.datasets.get_rdataset('mtcars').data
# print(data)
# print(type(data))
# print(data.head())


# X = data['hp']      # 마력 -> 독립변수  대문자사용 관용적임
# y = data['mpg']     # 연비 -> 종속변수  소문자사용


# # 상수항 추가
# X = sm.add_constant(X)

# # 모델 생성 및 학습
# # - 알고리즘 선택
# # - 모델 학습 => 그래프 찾기
# model = sm.OLS(y, X).fit()

# print(model.summary())

# # print('모델 계수 -----------')
# # print(model.params['hp'])      # 기울기
# # print(model.params['const'])      # 절편

# # print(model.params.iloc[1])      # 기울기
# # print(model.params.iloc[0])      # 절편

# print(type(model.params))



data = sm.datasets.get_rdataset('mtcars').data
print(data.head())

X = data[['hp', 'wt']]      # 마력,중량 -> 독립변수  대문자사용 관용적임
y = data['mpg']     # 연비 -> 종속변수  소문자사용

# 상수항 추가
X = sm.add_constant(X)

# 모델 생성 및 학습
# - 알고리즘 선택
# - 모델 학습 => 그래프 찾기
model = sm.OLS(y, X).fit()

print(model.summary())

print('모델 계수 -----------')

print(model.params)

