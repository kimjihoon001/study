# radio.py

from tkinter import Tk
from tkinter import Button
from tkinter import Radiobutton
from tkinter import IntVar


oroot = Tk() # 부모 윈도우
oroot.geometry("400x300")


radio_value=IntVar()    # 정수형 변수 생성
radio_value.set(-1)      # 정수값 설정



lunch= {0:'A런치',1:'B런치',2:"C런치"}


# variable => 클릭된 버튼의 정보를 지정한 변수명 설정
# value => radio_value에 저장된 데이터 지정하는 인수
orb1=Radiobutton(oroot,text=lunch[0],variable=radio_value,value=0)
orb2=Radiobutton(oroot,text=lunch[1],variable=radio_value,value=1)
orb3=Radiobutton(oroot,text=lunch[2],variable=radio_value,value=2)
orb1.pack()
orb2.pack()
orb3.pack()

def buy():
    value=radio_value.get()
    print(lunch[value])

obtn=Button(oroot,text='주문', command=buy)

obtn.pack()

oroot.mainloop()
