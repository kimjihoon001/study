# pd_data.py

import pandas as pd

## 데이터 분석
# csv 파일 데이터 읽기
path = r'ch18\pandas\data.csv'
df_csv = pd.read_csv(path)
# print(type(df_csv))
# print(df_csv)


print('-----------')

# Excel 파일 데이터 읽기
path = r'ch18\pandas\data.xlsx'
df_xl = pd.read_excel(path)
# print(type(df_xl))
# print(df_xl)

print('-------------')

# print(df_csv.head(3))
# print(df_csv.tail(1))

# 데이터 요약 정보
# df_csv.info()

# # 기술 통계량 정보
# print(df_csv.describe())

# # 기술 통계량 정보
# print(df_csv.sample())

# print(df_csv.sample(frac=0.5))


## 데이터 조작
