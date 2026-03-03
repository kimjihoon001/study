#tkinter_module.py

# from tkinter import *

# # 1. 위젯 생성
# otk=Tk()        #부모 윈도우(위젯)
# obtn=Button(otk, text="Click")   #자식버튼 위젯

# # 2. 위젯 패치
# obtn.pack()

# # 3. 이벤트 바인딩
# # Button(command=함수명)

# # # 위젯 동작 및 유지
# otk.mainloop()


from tkinter import *

def hi():
    print("hi there")

otk=Tk()
otk.geometry("400x300+980+400")       
obtn=Button(otk, text="Click",command=hi) 
obtn.pack()
otk.mainloop()