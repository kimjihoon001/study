#bindEvent.py

# from tkinter import Tk, Button

# # event: 이벤트 정보 객체(자동 전달)
# # def 함수명(event): 
# #   코드블록

# def order(event):
#     print("주문하세요")
    
# otk=Tk()
# otk.geometry("400x300")
# obtn=Button(otk,text="주문")

# # 객체명.bind("이벤트 문자열",함수객체)
# obtn.bind("<Button-1>",order)

# obtn.pack()
# otk.mainloop()

# tkinter 주요 이벤트 종류
# Tkinter 주요 이벤트 종류
# 이벤트            설명                  예시
# -------------------------------------------------------
# <Button-1>        마우스 왼쪽 버튼 클릭     Button-1 = 왼쪽, Button-2 = 가운데, Button-3 = 오른쪽
# <Double-Button-1> 마우스 더블 클릭          Double-Button-1 = 왼쪽 더블클릭
# <ButtonRelease-1> 마우스 버튼 뗌            왼쪽 버튼을 뗄 때
# <Motion>          마우스 움직임             마우스 커서 움직임 감지
# <Enter>           마우스 커서 위젯 진입      커서가 위젯 영역에 들어왔을 때
# <Leave>           마우스 커서 위젯 벗어남    커서가 위젯 영역 벗어날 때
# <Key>             키 입력                   모든 키 입력 감지
# <KeyPress-a>      특정 키 입력              'a' 키를 누를 때
# <KeyRelease>      키 뗌                     키에서 손 뗄 때
# <FocusIn>         포커스 들어옴             위젯이 입력 포커스 받음
# <FocusOut>        포커스 나감               위젯에서 포커스 나감
# <Configure>       위젯 크기/위치 변경        창 크기 변경 등
# <Destroy>         위젯 삭제                 윈도우 종료나 위젯 제거 시

from tkinter import Tk, Button
from tkinter import Label

def msg():
    print("start tkinter")
    
otk=Tk()
otk.geometry("300x300")


obtn=Label(otk,text="시작레이블") 
obtn.pack(side='top')

obtn=Button(otk,text="시작버튼",command=msg)
obtn.pack(side='bottom')

otk.mainloop()