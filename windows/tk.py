from tkinter import *


def Call():
    num: str = name.get()
    msg = Label(window, text=f"Hello, {num}")
    msg.place(x=365, y=20)
    button["bg"] = "orange"
    button["fg"] = "white"
    button["text"] = "Saved"


window = Tk()
window.title("Test window")
window.geometry("800x600")
window.configure(background = "black")
logo = PhotoImage(file="logo.gif")
logo_image = Label(image=logo)
logo_image.place(x=0, y=0, width=800, height=600)
name = Entry(text=0)
name.insert(0, 'Username')
name.place(x=360, y=60, width=100, height=25)
button = Button(text="Save it!", command=Call)
button.place(x=360, y=100, width=100, height=25)
window.mainloop()
