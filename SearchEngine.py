import tkinter
import sqlite3
from sqlite3 import Error
def create_connection(db_file):

    conn = None
    try:
        conn= sqlite3.connect(db_file)
        print(e)
    return conn



def select_all_books(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")

    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_name(conn, name):
    cur = conn.cursor()
    cur.execute("Select *from books where name=?",(name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_type(conn, type):
    cur = conn.cursor()
    cur.execute("Select *from books where type=?",(type,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_book_by_author(conn, author):
    cur = conn.cursor()
    cur.execute("Select *from books where author=?",(author,))
    rows = cur.fetchall()
    for row in rows:
        print(row)                

def select_book_by_year(conn, year):
    cur = conn.cursor()
    cur.execute("Select *from books where year=?",(year,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    #database = add later

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