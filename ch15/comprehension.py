# comprehension.py

# 리스트 컴프리헨션
# [표현식 for 요소 in 이터러블 [if 조건]]

numbers = [1, 2, 3, 4]
squared = [x**2 for x in numbers]
print(squared)
print(type(squared))

squared = [x for x in numbers if x%2==0]
print(squared)

squared = [x**2 for x in numbers if x%2==0]
print(squared)

squared = [x**2+1 for x in numbers if x%2==0]
print(squared)

print('------------')
# 딕셔너리 컴프리핸션
# {key:value, key:value, key:value,}
# {key 표현식:value표현식for 요소 in 이터러블 [if 조건]}

squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)

squared_dict = {x: x**2 for x in range(5) if x%2==0}
print(squared_dict)

subjects = ['math','english','history']

scores={subject:0 for subject in subjects}
print(scores)

print('-------------')

# 제너레이터 생성 방법2
# 제너레이터 컴프리핸션
# (표현식 for 요소 in 이터러블 [if 조건])

gen = (i*i for i in range(1,10))
print(next(gen))
print(next(gen))
for item in gen:
    print(item)
print(next(gen))    #StopIteration
