import tkinter as tk
from playsound import playsound


root=tk.Tk()
root.title("Fix Speakers")
root.configure(background="Black")
root.geometry("200x100+10+10")



def fonk1():
    playsound("ses.mp3")

buton=tk.Button(text="Fix it",command=fonk1)
buton.pack()

yazı=tk.Label(text="--Coded By Emyounoone--",bg="black",fg="red")
yazı.pack(side="bottom")

root.mainloop()

