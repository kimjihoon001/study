# rev_iterator.py

class Rev_iterator:
    pass

    def __init__(self,data):
        self.data = data
        self.poistion = len(self.data)-1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.poistion < 0:
            raise StopIteration
        
        result = self.data[self.poistion]
        self.poistion -= 1
        return result


a = Rev_iterator([1,2,3])    
ia = iter(a)
print(type(ia))

print(next(ia))
print(next(ia))
print(next(ia))


# 이터레이터 판단 기준
# 런타임에서 객체를 보고 이터레이터 규칙을 만족하는 확인
# 즉, 객체에 다음 매서드가 있으면 이터레이터 인식
# __inter__
# __next__

print('-----------------')
print(dir(ia))
print('__inter__'in dir(ia))
print('__next__'in dir(ia))