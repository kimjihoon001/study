# label_image.py
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import PhotoImage


# from PIL import Image

# image=Image.open(r"경로.jpg")
# img_resized=image.resize((300,200))
# image.save(r"경로.png")

oroot=Tk()
oroot.geometry("800x600")

img1= PhotoImage(file=r"ch11\widget2\apple.png")
img_label=Label(oroot, image=img1)
img_label.place(x=-20,y=-20)
obutton1=Button(oroot,text="PUSH1")
obutton2=Button(oroot,text="PUSH2")
obutton3=Button(oroot,text="PUSH3")
obutton1.place(x=10,y=60)
obutton2.place(x=140,y=60)
obutton3.place(x=80,y=10)
oroot.mainloop()

