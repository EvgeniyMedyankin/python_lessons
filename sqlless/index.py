import sqlite3

db_name = "test1.db"
with sqlite3.connect(db_name) as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users( id integer PRIMARY KEY AUTOINCREMENT, first_name text NOT NULL, 
last_name text NOT NULL, age integer);""")


def user_data():
    first_name = input("Enter first_name: ")
    last_name = input("Enter last_name: ")
    age = input("Enter age: ")
    cursor.execute("""INSERT INTO users(first_name, last_name, age) VALUES(?, ?, ?)""",
                   (first_name, last_name, age))
    db.commit()


def get_users():
    cursor.execute("SELECT * FROM users")
    for x in cursor.fetchall():
        print(x[1])


def remove_user(user_name: str):
    cursor.execute(f"DELETE employees WHERE id={user_name}")


# user_data()
get_users()

db.close()
