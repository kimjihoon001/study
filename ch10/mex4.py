# 클래스 정의
class Cvalue:

    def __init__(self):
        self.lista=[]
    def add(self, num):
        self.lista.append(num)
    def fprint(self):
        print(self.lista)

# 함수정의
def plus(a,b):
    c = a + b
    return c

if __name__ == '__main__':
    p1=Cvalue()
    p1.add(1)
    p1.add(2)
    p1.add(3)
    p1.fprint()


print(__name__)