# Bag.py

class Bag:
    #맴버 변수
    # color = "검정색"
    # data = []
    #메서드
    def __init__(self,name,color):
        self.name = name
        self.data = []
        self.color=color
        
    def add(self, x):
        self.data.append(x)
    def addtwice(self,x):
        self.add(x)
        self.add(x)


shoulder =Bag("sholuder","black")
print(shoulder.color)
shoulder.add("휴대폰")
print(shoulder.data)
shoulder.addtwice("돈")
print(shoulder.data)
print(shoulder.name)

hand = Bag("hand","white")
print(hand.color)
print(hand.name)
print(hand.addtwice("돈"))
print(hand.data)
