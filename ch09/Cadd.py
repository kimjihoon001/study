#Cadd.py

class Cadd:
    def fadd(self,a,b):
        self.x=a
        self.y=b
        self.hap=self.x+self.y

obj=Cadd()
obj.fadd(10,20)
print("x: ",obj.x)
print("y: ",obj.y)
print("x + y : ",obj.hap)