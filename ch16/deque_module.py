# deque_module.py

from collections import deque

dq = deque()    # 덱 생성

dq.append(1)    # dq 오른쪽으로 데이터 삽입
print(dq)

dq.appendleft(2) # dq 왼쪽으로 데이터 삽입
print(dq)

dq.pop()        # 오른쪽 데이터 꺼내기
print(dq)

dq.popleft()    # 왼쪽 데이터 꺼내기
print(dq)

print(type(dq))

# 리스트와 댁의 내부 구조 비교
# list 구조 : 동적 배열 구조
list_a = [10, 20, 30, 40]
print(list_a)
# 삽입/삭제시 요소 이동 발생

# 덱 구조: 블록기반 이중 연결 구조
# [block]<->[block]<->[block]
# block 내부
# [10][20][30]
# 삽입 /삭제시 요소 이동 발생 안함 