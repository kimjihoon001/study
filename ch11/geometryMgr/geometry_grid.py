# geometry_pack.py

from tkinter import Tk, Button

otk=Tk()
otk.title("배치 학습")

otk.geometry("400x300")       
obtn1=Button(otk, text="PSUH1")
obtn2=Button(otk, text="PUSH2")  
obtn3=Button(otk, text="PUSH3")
obtn4=Button(otk, text="PUSH4") 
# 2. 위젯 배치
obtn1.grid(row=0,column=1)
obtn2.grid(row=1,column=0)
obtn3.grid(row=3,column=1)
obtn4.grid(row=1,column=3)

otk.mainloop()