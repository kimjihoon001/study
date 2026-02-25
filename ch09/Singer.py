#클래스(분류:가수) 정의
class Singer:
    #(클래스)맴버 변수
    name="아이유"
    def sing(self):
        self.name="IU" #(인스턴스) 맴버 변수
        print("이 밤 그날의 반딧불의 당신의~")
        
iu=Singer()
iu.sing()
print(iu.name)
print(Singer.name)

print('----------')

bts =Singer()
print(bts.name)
print(bts.sing())