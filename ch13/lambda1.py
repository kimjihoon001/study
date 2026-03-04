# lambda1.py

# lambda 인자 : 표현식

# 일반적 함수 정의 및 호출

# def 함수명(매개변수):
#     코드블록
#     return 반환값

# 함수명(인수)

# def add(x):
#     return x+x
# add(1)
# add(2)
# add(3)

print('---------')

# 람다 함수의 정의 및 호출

# add = lambda x : x+x
# print(add(1))
# print(add(2))
# print(add(3))

print((lambda x : x+x)(1))
print((lambda x : x+x)(2))
print((lambda x : x+x)(3))


square=lambda x : x**2
print(square(3))

print((lambda x: x**2)(4))

print('------------')

#lambda 매개1, 매개2 : 표현식

adder = lambda x,y=5 : x+y
print(adder(3))
print(adder(3,10))
print((lambda x,y : x+y)(3,10))
print((lambda x,y=5 : x+y)(3))