# entry.py
# 엔트리 위젯
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar

otk=Tk()
otk.geometry("400x300")   

# (문자열) 변수 값 위젯과 연결 가능
ostring = StringVar() 

# textvariable : 값 변화 자동 반영   
oentry=Entry(otk, textvariable=ostring)
olabel=Label(otk, textvariable=ostring,bg="red")



# 2. 위젯 배치
oentry.pack()
olabel.pack()

otk.mainloop()