# generator.py

def simple_generator():
    yield 'a'
    yield 'b'
    yield 'c'
    
g = simple_generator()
print(type(g))

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for item in g:
    print(item)
    
print('-----------------')
# dir(): 객체의 속성을 보여주는 함수
print(dir(g))
print('__inter__'in dir(g))
print('__next__'in dir(g))

# 제너레이터는 이터레이터의 한 종류

def mygen():
    for i in range(1,1000):
        result = i * i
        yield result

gen = mygen()
print(next(gen))
print(next(gen))
print(next(gen))