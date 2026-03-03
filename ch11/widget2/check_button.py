# checkbutton.py

from tkinter import Tk
from tkinter import Button
from tkinter import BooleanVar
from tkinter import Checkbutton

oroot = Tk() # 부모 윈도우
oroot.geometry("400x300")


check_value={}
coffee= {0:'아메리카노',1:'라떼',2:"카푸치노",3:'에스프레소'}

for i in range(len(coffee)):
    check_value[i]=BooleanVar()
    ocheckbutton1= Checkbutton(oroot,text=coffee[i],variable=check_value[i])
    ocheckbutton1.pack()

def buy():
    for i in check_value:
        if check_value[i].get() == True:
            print(coffee[i])
   


obtn=Button(oroot,text='주문', command=buy)
obtn.pack()


oroot.mainloop()