# label.py
from tkinter import Tk, Label

otk=Tk()
otk.geometry("400x300")       
olabel=Label(otk,text="적",bg="red",width=20)
olabe2=Label(otk,text="적",bg="green",width=20)
olabe3=Label(otk,text="적",bg="blue",width=20)


# 2. 위젯 배치
olabel.pack()
olabe2.pack()
olabe3.pack()

otk.mainloop()