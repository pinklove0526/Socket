from tkinter import *
import mysql.connector

def create_connection(db_file):
    db_file = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    print(db_file)

def select_all_books(conn,database):
    conn = mysql.connector.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_name(conn, name, database):
    conn = mysql.connector.connect(database)
    cur = conn.cursor()
    cur.execute("select * from books where name=?",(name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_type(conn, type, database):
    conn = mysql.connector.connect(database)
    cur = conn.cursor()
    cur.execute("select * from books where type = ?",(type,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_author(conn, author, database):
    conn = mysql.connector.connect(database)
    cur = conn.cursor()
    cur.execute("select * from books where author = ?",(author,))
    rows = cur.fetchall()
    for row in rows:
        print(row)                

def select_book_by_year(conn, year, database):
    conn = mysql.connector.connect(database)
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
    edit = Entry(fram)
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    edit.focus_set()
    butt = Button(fram, text="Search")
    butt.pack(side=RIGHT)
    fram.pack(side=TOP)
    OPTIONS = ["Name", "Type", "Author", "Year", "All books"]
    global v
    v = StringVar(root)
    v.set(OPTIONS[0])
    w = OptionMenu(root, v, *OPTIONS)
    w.pack()
    database = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    conn = create_connection(database)
    print(" All books")
    select_all_books(conn, database)

def find():
    text.tag_remove('Found', '1.0', END)
    s = edit.get()
    if s:
        idx = 1.0
        while 1:
            idx = text.search(s, idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))
            text.tag_add('found', idx, lastidx)
            idx = lastidx
            text.tag_config('found', foreground='red')
            edit.focus_set()
            butt.config(command=find)

def main():
    database = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
    conn = create_connection(database)
    with conn:
        print("Book by name:")
        select_book_by_name(conn, x)
        print("Book by type:")
        select_book_by_type(conn, x)
        print("Book by author:")
        select_book_by_author(conn, x)
        print("Book by year:")
        select_book_by_year(conn, x)
        print(" All books")
        select_all_books(conn)

main_screen()
root.mainloop()