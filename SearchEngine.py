from tkinter import *
import mysql.connector

def create_connection(db_file):
    db_file = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    print(db_file)

def main():
    database = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    conn = create_connection(database)
    main_screen()

def select_all_books():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_name():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    cur = conn.cursor()
    cur.execute("select * from books where name like %%")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_type():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    cur = conn.cursor()
    cur.execute("select * from books where type = ?")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_author():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    cur = conn.cursor()
    cur.execute("select * from books where author = ?",(author,))
    rows = cur.fetchall()
    for row in rows:
        print(row)                

def select_book_by_year():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    cur = conn.cursor()
    cur.execute("select * from books where year = ?",(year,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main_screen():
    global root
    root = Tk()
    fram = Frame(root)
    Label(fram, text='Book to find:').pack(side=LEFT)
    global inp
    inp = StringVar()
    edit = Entry(fram, textvariable=inp)
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    edit.focus_set()
    butt = Button(fram, text="Search", command=find)
    butt.pack(side=RIGHT)
    fram.pack(side=TOP)
    global OPTIONS
    OPTIONS = ["Name", "Type", "Author", "Year", "All books"]
    global v
    v = StringVar(root)
    global w
    w = OptionMenu(root, v, *OPTIONS)
    w.pack()
    select_all_books()

def find():
    inp2 = inp.get()
    v2 = v.get()
    if v2 == "Name": select_book_by_name()
    elif v2 == "Type": select_book_by_type()


main()
root.mainloop()
