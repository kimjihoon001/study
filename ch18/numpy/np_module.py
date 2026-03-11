# np_module.py

import numpy as np

arr = np.array([1,2,3,4,5]) # 1차원 벡터


print(type(arr))
print(arr)

print(arr.shape)    # 배열 모양(크기)
print(arr.dtype)    # 데이터 타입


print('0으로 초기화된 배열 ---------')
zeros = np.zeros((3,3))

print(type(zeros))
print(zeros)

print('1으로 초기화된 배열 ---------')
ones = np.ones((3,3))

print(type(ones))
print(ones)
print(ones.shape)
print(ones.dtype)

print('특정 값으로 초기화된 배열 ---------')
full = np.full((2,2),7,dtype=float)
print(full.dtype)


print('단위 행렬 -----------')
print(np.eye(2,3))
print(np.eye(4))
print(np.identity(3))


print('난수 배열-----------')

random = np.random.rand(3,3)
print(random)
print(random.shape)
print(random.dtype)


randint = np.random.randint(1,10,(3,3))
print(randint)
print(randint.shape)
print(randint.dtype)

print('기본 산술 연산 ------------')
arr = np.array([1,2,3,4])
print(arr+5)
print(type(arr+5))
print(arr*2)

print('통계 함수 ---------------')
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())

# 파이썬 list 
# - 내장 자료형 
# - 다양한 자료형 사용가능

# numpy array 
# - 외장 자료형
# - 동일 자료형 사용 가능



print('브로드캐스팅 =============')

arr1 = np.array([1,2,3])    # 행 벡터 (3,)
print(arr1)
print(arr1.shape)
arr2 = np.array([[1],[2],[3]])  # 열 벡터 (3,1)
print(arr2)
print(arr2.shape)


# 브로드캐스팅(virtual expansion)
# : 자동으로 (모양을 ) 맞춰서 늘려준다.
# arr1은 1차원이지만 연산자 (1,3)처럼 동작

result = arr1 + arr2
print(result)
print(result.shape)
#   [ [1 2 3]       [[1 1 1]         [[2 3 4]   
    # [1 2 3]   +   [2 2 2]   =      [3 4 5]  
    # [1 2 3]]      [1 2 3]]         [4 5 6]]    


print('------------')

# 행렬 곱

matrix1 = np.array([[1,2],[3,4]])
print(matrix1)
matrix2 = np.array([[5,6],[7,8]])
print(matrix2)
result = np.dot(matrix1,matrix2)
print(result)



print('기본 인덱싱=============')
arr = np.array([10,20,30,40])
print(arr[2])

arr = np.array([[1,2,3],[3,4,5]])
print(arr)
print(arr[1,2])


print('슬라이싱 ============')
print(arr[0,0:3])
print(arr[0,:])
print(arr[:,1])

print('조건부 연산 =============')
arr = np.array([1,2,3,4,5])
filtered = arr[arr>3]
print(filtered)

import pandas as pd

df = pd.DataFrame(arr, columns=['Value'])
print(df)