#Human.py

class Human:
    def __init__(self,age,name):
        self.age = age      #인스턴스 변수
        self.name = name
    #기능 : 자기소개하다
    def intro(self):
        print(str(self.age)+"살",end=" ")
        print(self.name)
        
# 객체 생성        
kim=Human(29,"김상현")
lee=Human(45,"이승우")

# 객체 접근(함수 호출)
kim.intro()
lee.intro()

# 정수 10을 na 변수명으로 할당
na = 10     
# 정수 객체 => 클래스로 생성됨
print(type(na))
# int() => 생성자 함수
na = int(10)

print(type(na))

float()
str()
bool()
list()
dict()
tuple()