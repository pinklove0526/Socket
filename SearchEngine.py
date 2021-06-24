import tkinter
import sqlite3
from sqlite3 import Error
def create_connection(db_file):

    
    
        db_file = sqlite3.connect(host="localhost", user="root", passwd="", database="Online_Library")
        print(db_file)
    



def select_all_books(conn,database):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_name(conn, name, database):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("Select *from books where name=?",(name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_type(conn, type, database):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("Select *from books where type=?",(type,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_author(conn, author, database):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("Select *from books where author=?",(author,))
    rows = cur.fetchall()
    for row in rows:
        print(row)                

def select_book_by_year(conn, year, database):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("Select *from books where year=?",(year,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    database = sqlite3.connect(host="localhost", user="root", passwd="", database="Online_Library")
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