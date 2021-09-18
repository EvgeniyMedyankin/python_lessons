from tkinter import *
import sqlite3
import os

db_name = "test1.db"
with sqlite3.connect(db_name) as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users( id integer PRIMARY KEY AUTOINCREMENT, first_name text NOT NULL, 
last_name text NOT NULL, age integer);""")


def get_users():
    cursor.execute("SELECT * FROM users")
    for x in cursor.fetchall():
        print(x[1])


def remove_user():
    user_list = cursor.execute("SELECT id FROM users ORDER BY id DESC")
    users = user_list.fetchall()
    if len(users) == 0:
        msg = Label(window, text=f"None")
        msg.place(x=330, y=20)
        db.close()
    current_user: int = int(users[0][0])
    cursor.execute("DELETE FROM users WHERE id=?", [current_user])
    """Send notification in OS : libnotify-bin"""
    os.system(
        f"notify-send \"Remove user\" \"User {current_user} succesfully removed\" -t 5000 -i folder-gitlab -a WebApp -u critical")
    return get_users()


def save():
    name: str = first_name.get()
    surname: str = last_name.get()
    user_age: str = age.get()
    user: object = {
        first_name: name,
        last_name: surname,
        age: user_age
    }
    """Save data to DB"""
    cursor.execute("""INSERT INTO users(first_name, last_name, age) VALUES(?, ?, ?)""", (name, surname, user_age))
    db.commit()

    msg = Label(window, text=f"Hello, {name}. Data saved!")
    msg.place(x=330, y=20)
    save_button["bg"] = "green"
    save_button["fg"] = "white"
    save_button["text"] = "Saved"


window = Tk()
window.title("Users List")
window.geometry("800x600")
window.configure(background="black")

logo = PhotoImage(file="logo.gif")
logo_image = Label(image=logo)
logo_image.place(x=0, y=0, width=800, height=600)

first_name = Entry(text=0)
first_name.insert(0, 'First name')
first_name.place(x=360, y=60, width=100, height=25)

last_name = Entry(text=1)
last_name.insert(1, 'Last name')
last_name.place(x=360, y=90, width=100, height=25)

age = Entry(text=2)
age.insert(2, 'Age')
age.place(x=360, y=120, width=100, height=25)

save_button = Button(text="Save it!", command=save)
save_button.place(x=360, y=160, width=100, height=25)

remove_button = Button(text="Remove last", command=remove_user)
remove_button.place(x=360, y=190, width=100, height=25)

window.mainloop()
