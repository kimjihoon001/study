# pd_data1.py

import pandas as pd

data = {
    'ID': [1,2,3],
    'Name': ['Alice','Bob','Charlie'],
    'Age': [30,35,25]
}
df = pd.DataFrame(data)
print(df)


print('열 선택 -----------')
print(df['Name'])


print('조건 필터링 -----------')
print(type(df['Age'] > 30))   #Series
print('------------')
print(df[df['Age']>30])   #DataFrame

print('데이터 정렬 ---------------')

sorted_df = df.sort_values(by='Age',ascending= False)

print(sorted_df)

# 열 추가
df['Salary'] = [5000, 6000, 7000]
print(df)

# 행 추가
# df.loc[3] = [4,'David',40,2000]
df.loc[len(df)] = [4,'David',40,2000]
print(df)
print('행 삭제 -------------')
df = df.drop(1)
print(df)
# 행 번호 주의
# print(len(df)) # 3
# df.loc[len(df)] = [5,'Eva',50,9000]
# print(df)

print('재정렬 ------------')
# index 재정렬
df1 = df.reset_index(drop=True)
print(df1)

print('------------')

data2 = {
    'ID': [5, 6],
    'Name': ['Eva', 'Frank'],
    'Age': [28, 33]
}

df2 = pd.DataFrame(data2)

print('데이터 연결------------')

concated = pd.concat([df,df2],ignore_index=True)
print(concated)

print('데이터 병합 ---------------')
data3 = {
    'ID': [1,2,3,4,5,6],
    'Department': [
                    'HR',
                    'Enginering',
                    'Sales',
                    'R&D',
                    'Finance',
                    'Sales'
                ]
}
df3 = pd.DataFrame(data3)
merged = pd.merge(concated, df3)
print(merged)

# 데이터 처리
print('결측치 정리 --------------')

print(merged.isnull().sum())


# 결측치 채우기
meanVal = merged['Salary'].mean()
print(meanVal)

merged['Salary'] = merged['Salary'].fillna(meanVal)
print(merged)

print("중복 데이터 처리 ----------")
data1 = {
    'ID': [1,3],
    'Name':['Alice','Charlie'],
    'Age':[30, 25],
    'Salary': [5000, 7000],
    'Department': ['HR', 'Sales']
}

df1 = pd.DataFrame(data1)
df1 = pd.concat([merged,df1])
print(df1)


print('-----------------')
print(df1.duplicated())

df1_1 = df1.drop_duplicates()
print(df1_1)


help(object)
