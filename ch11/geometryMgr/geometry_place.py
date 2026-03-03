# geometry_pack.py

from tkinter import Tk, Button

otk=Tk()
otk.title("배치 학습")

otk.geometry("400x300")       
obtn1=Button(otk, text="PSUH1")
obtn2=Button(otk, text="PUSH2")  
obtn3=Button(otk, text="PUSH3") 
# 2. 위젯 배치
obtn1.place(x=10,y=60)
obtn2.place(x=140,y=60)
obtn3.place(x=150,y=60)

otk.mainloop()

# ** 배치 매니저 혼합 사용 주의 사항
# pack()과 grid() 혼합 사용 불가
# grid()와 place() 혼합 사용 불가