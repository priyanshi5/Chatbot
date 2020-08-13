from tkinter import *
from PIL import ImageTk, Image


def yes():
    root.destroy()
    import Chatb

def no():
    root.destroy()



root=Tk()
root.title("chatbot project 2")
root.geometry("800x600")
root.resizable(0,0)


photo=PhotoImage(file="bot.png")
Label(root,image=photo).pack()



f1=Frame(root,bg="black").pack()
Label(f1,fg="white",bg='black',font=("arial",30,'bold'),text="Excited to talk to bot??").place(x=225,y=200)

f2=Frame(root,bg="red").pack()
Button(f2,fg="white",bg='red',font=("arial",25,'bold'),text="Yes",command=yes).place(x=220,y=350)

f3=Frame(root,bg="red").pack()
Button(f3,fg="white",bg='red',font=("arial",25,'bold'),text="No",command=no).place(x=530,y=350)


root.mainloop()