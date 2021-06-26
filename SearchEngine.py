from tkinter import *
import tksheet
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

def select_book_by_name(name):
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE Name LIKE %s", (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_type(booktype):
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE Type LIKE %s", (booktype))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_author(author):
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE Author LIKE %s", (author,))
    rows = cur.fetchall()
    for row in rows:
        print(row)                

def select_book_by_year(year):
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE YEAR = %s", (year,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main_screen():
    global root
    root = Tk()
    fram = Frame(root)
    Label(fram, text='Tim sach: ').pack(side=LEFT)
    global inp
    inp = StringVar()
    edit = Entry(fram, textvariable=inp)
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    edit.focus_set()
    butt = Button(fram, text="Tim", command=find)
    butt.pack(side=RIGHT)
    fram.pack(side=TOP)
    global OPTIONS
    OPTIONS = ["Name", "Type", "Author", "Year"]
    global v
    v = StringVar(root)
    global w
    w = OptionMenu(root, v, *OPTIONS)
    w.pack()
    select_all_books()

def find():
    inp2 = inp.get()
    v2 = v.get()
    if v2 == "Name": select_book_by_name(inp2)
    elif v2 == "Type": select_book_by_type(inp2)
    elif v2 == "Author": select_book_by_author(inp2)
    elif v2 == "Year": select_book_by_year(inp2)

main()
root.mainloop()