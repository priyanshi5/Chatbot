from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import speech_recognition as sr
import pyttsx3
import win32api
from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as mb

eng=pyttsx3.init()
voices=eng.getProperty('voices')
print(voices)

eng.setProperty('voice',voices[1].id)

eng.setProperty('rate', 150) 
# Set volume 0-1 
eng.setProperty('volume', 0.7)

def speak(word):
    eng.say(word)
    eng.runAndWait()

bot=ChatBot("Jarvis")

conversation=[
    "hi",
    "hello , how can I help you?",
    
    "good morning",
    "good morning",

    "Good night",
    "Good night",

    "what is your name",
    "My name is Jarvis , how can I help you?",

    "how are you",
    "I am fine",

    "in which language do you speak",
    "English",
]

trainer=ListTrainer(bot)
trainer.train(conversation)


     

def New():
    mb.showinfo("welcome","You want new file")
    root.destroy()
    import new 

def Back():
    root.destroy()
    import phy

def Next():
    root.destroy()
    import his
    




root=Tk()
root.title("Jarvis")
menu=Menu(root)
root.config(menu=menu)
root.geometry("850x725")
root.resizable(0,0)

'''photo=ImageTk.PhotoImage(file="jarv.jpeg")
photo_image=Label(root,image=photo).pack()'''

f1=Frame(root,bd=15,bg="black",relief=RIDGE,height=220,width=850).pack(side=TOP)

img = PhotoImage(file="6.png")

PhotoL = Label(image=img,height=100,width=400).place(x=15,y=15,height=190)


Label(f1,text="JARVIS",fg="white",bg="black",font=("arial",35,'bold')).place(x=550,y=60,height=100)
Label(f1,bg="white").place(x=20,y=222,height=3,width=780)
f2=Frame(root,bd=15,bg="maroon",relief=RIDGE).place(x=0,y=220,width=850,height=450)
f3=Frame(root,bd=15,bg="maroon",relief=RIDGE).place(x=0,y=670,height=96,width=850)




def chatting():
    quary=e1.get()

    answer_from_bot=bot.get_response(quary)
    textarea.insert(END,"\nYou : " + quary)
    textarea.insert(END,"\n\t\t\tJarvis : "+ str(answer_from_bot))
    speak(answer_from_bot)
    e1.delete(0,END)
    textarea.yview(END)


scrollbar = Scrollbar(f2)
scrollbar.place(x=815,y=230,height=430)

textarea = Text(f2, yscrollcommand = scrollbar.set,fg='blue',font='arial 12 bold',bg="white" )


image=Image.open("cartoon.jpg")
m=ImageTk.PhotoImage(image)
Label(textarea,image=m).pack(side=RIGHT)

textarea.place(x=12,y=230,width=800,height=430)
scrollbar.config( command = textarea.yview )

e1=Entry(f3,fg="black",font=("arial",20),bg="white")
e1.place(x=12,y=680,width=695,height=70)
btn=Button(f3,text="Sumbit",fg="white",bg="sea green",font=("arial",20,'bold'),bd=7,command=chatting).place(x=710,y=680,height=75,width=120)





root.mainloop()




    