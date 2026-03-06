# gen_iter_class.py
# 제너레이터 생성 방법3: 클래스 정의

gen= (i*i for i in range(1,100))
print(type(gen))    #generator
for i in gen:
    print(i)
    
class Myiterator:
    
    def __init__(self):
        self.data = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.data * self.data
        if self.data >= 100:
            raise StopIteration
        self.data += 1
        return result
    
my_iter = Myiterator()
print(type(my_iter))
for i in my_iter:
    print(i)