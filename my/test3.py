# def calculate_average(num_list):
#     total=0
#     for num in num_list:
#         total += num
#     average = total/len(num_list)
#     return average

# num_list = [10, 20, 30, 40, 50]
# average = calculate_average(num_list)
# print("평균: ", average)


# def check_odd_even(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(check_odd_even(4))  
# print(check_odd_even(7))  


# my_dict={ 'a': 10, 'b': 20, 'c': 30 }

# def add_sum(my_dict):
#     total=0
#     for num in my_dict.values():
#         total += num
#     return total

# print(id(print(f"합은 {add_sum(my_dict)}")))

# class Phone:
#     def __init__(self,number,color):
#         self.number=number
#         self.color=color
#     def showInfo(self):
#         print("전화번호:",self.number)
#         print("색상:",self.color)
 
# class SmartPhone(Phone):
#     def __init__(self, number, color,company):
#         super().__init__(number, color)
#         self.company=company
#     def showInfo(self):
#         super().showInfo()
#         print("회사:",self.company)      
    
        
# apple = SmartPhone("010-1234-5678", "검정", "애플")
# apple.showInfo()

# from tkinter import Tk
# from tkinter import Label
# from tkinter import Checkbutton
# from tkinter import Button
# from tkinter import StringVar
# from tkinter import BooleanVar


# oroot = Tk()
# oroot.title("조각 피자 주문 프로그램")
# oroot.geometry('400x300')
# meuns = {'치즈 피자 (3200원)':3200, '콤비네이션 피자 (3500원)':3500, '불고기 피자 (3600원)':3600}
# Label(oroot,text='피자').pack()
# vars={}
# order_str=StringVar()

# for meun in meuns:
#     var=BooleanVar()
#     ocbt=Checkbutton(oroot, text=meun, variable= var)
#     ocbt.pack(anchor='w')
#     vars[meun]=var

# def order():
#     total=0
#     text='주문내역:\n'
#     for meun in meuns:
#         if vars[meun].get()==1:
#             text += f'-{meun}\n'
#             total += meuns[meun]
#     text+=f'\n총 가격: {total}원'
#     order_str.set(text)
        
# obt=Button(oroot,text='주문',command=order)
# obt.pack()
# order_label=Label(oroot,textvariable=order_str)
# order_label.pack()

# oroot.mainloop()


# class Student:
#     school = "High School"
    
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

# class test(Student):
#     pass

# s1= test('Alice', 1)

# print(Student.school)
# print(s1.school)
# print(s1.name)

# from math import factorial

# print("5! :",factorial(5))
# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
# s1=Dog()    
# print(s1.speak())



import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("알림", "버튼이 클릭되었습니다.")

root = tk.Tk()
root.title("간단한 Tkinter 앱")
root.geometry("300x200")

btn = tk.Button(root, text="클릭하세요", command=on_button_click)
btn.pack(pady=20)

root.mainloop()