from tkinter import *
from PIL import ImageTk




def yes():
    root.destroy()
    import Jarvis

root=Tk()
root.title("chatbot project 2")
root.geometry("1000x500")
root.resizable(0,0)




photo=PhotoImage(file="cb.png")
photo_image=Label(root,image=photo).pack()

f1=Frame(root,bg="black").pack()
Button(f1,fg="white",bg='black',font=("arial",25,'bold'),text="Talk to Bot",command=yes).place(x=350,y=400)



root.mainloop()