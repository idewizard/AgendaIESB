from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("400x400")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")



B = Button(top, text = "Cadastrar", command = helloCallBack)
B.place(x = 50,y = 50)


top.mainloop()