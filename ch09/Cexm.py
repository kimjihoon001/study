
class Cexm:
    #맴버 변수
    #맴버 함수
    def fsan(self):
        print("맴버 함수(메서드)")
    def fsbn(self, pa):
        self.x = pa
        print("맴버 변수 x: ",self.x)
        
ca =Cexm()
ca.fsan()
ca.fsbn(10)