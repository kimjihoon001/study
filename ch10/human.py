#Human.py

#super class
class Human:
    # 맴버 변수
    eyes=2
    nose=1
    mouth=1
    # 메서드
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print('이름:',self.name)
        print('나이:',self.age)
    def eat(self):
        print('먹다')
    def sleep(self):
        print('자다')
    def talk(self):
        print('말하다')

    

# #sub class
class Student(Human):
    #맴버 변수(속성)
    #메서드( 기능/ 동작)  
    def __init__(self,name,age,studentnum):
        # self.name=name
        # self.age=age
        super().__init__(name,age)
        self.studentnum=studentnum
    def introduce(self):
        # print('이름:',self.name)
        # print('나이:',self.age)
        super().introduce()
        print('학번:',self.studentnum)
    def study(self):
        print("공부하다")


lee = Human('이수근',49)
lee.introduce()
lee.eat()
lee.sleep()
lee.talk()
print('눈 개수:',lee.eyes)

kim=Student('김호동',54,282828)
kim.study()
kim.introduce()
kim.eat()
print('눈 개수:',kim.eyes)
    
choi = Student("최민식",18,151515)
choi.introduce()
choi.study()
choi.eat()
print("학번",choi.studentnum)