from tkinter import *


def Call():
    num: str = name.get()
    msg = Label(window, text=f"Hello, {num}")
    msg.place(x=100, y=20)
    button["bg"] = "orange"
    button["fg"] = "white"
    button["text"] = "Pressed"


window = Tk()
window.geometry("300x200")
name = Entry(text=0)
name.place(x=100, y=80, width=100, height=25)
button = Button(text="Press me", command=Call)
button.place(x=100, y=120, width=100, height=25)
window.mainloop()
