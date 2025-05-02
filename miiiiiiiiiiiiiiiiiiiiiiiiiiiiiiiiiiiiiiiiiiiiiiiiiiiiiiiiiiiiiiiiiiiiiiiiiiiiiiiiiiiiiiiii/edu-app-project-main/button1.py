from tkinter import *
from tkinter import messagebox
tk = Tk()
tk.geometry("100x100")
def helloCallBack():
    msg=messagebox.showinfo("Hello Python", "Hello World")
B = Button(tk, text ="Hello", command = helloCallBack)
B.place(x=50,y=50)
tk.mainloop
