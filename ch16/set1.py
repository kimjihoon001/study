# set1.py

numbers = {1, 2, 3, 3, 4}

print(type(numbers))
print(numbers)

# 요소 추가 및 제거
numbers.add(5)
numbers.remove(3)
print(numbers)

# 집합 연산
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 & set2)
print(set1 | set2)
print(set1 - set2)