# iterable1.py

a = [1,2,3]
# next(a)
# 'list' object is not an iterator

# 이터레이터 생성 방법1
ia = iter(a)
print(type(ia))

# print(next(ia))
# print(next(ia))
# print(next(ia))
# print(next(ia))     #StopIteration


for i in ia:
    print(i)
    
for i in ia:
    print(i)