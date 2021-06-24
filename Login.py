from tkinter import *
import tkinter.messagebox
import mysql.connector

db_conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Online_Library")
cursordb = db_conn.cursor()
 
def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Dang nhap tai khoan")
    root2.geometry("450x300")
    root2.config(bg="white")
    global username_verification
    global password_verification
    Label(root2, text='Vui long nhap vao thong tin tai khoan', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white", bg="blue",width=300).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Tai khoan*", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=username_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Mat khau*", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Dang nhap", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=login_verification).pack()
    Label(root2, text="")

def register_screen():
    global reg_message
    reg_message = Toplevel(root)
    reg_message.title("Dang ky")
    reg_message.geometry("450x300")
    reg_message.config(bg="white")
    global uname
    global pw
    uname = StringVar()
    pw = StringVar()
    Label(reg_message, text="Nhap thong tin duoi day de dang ky", bd=5, font=('arial', 12, 'bold'), relief="groove", fg="white", bg="blue", width=300).pack()
    Label(reg_message, text="").pack()
    Label(reg_message, text="Tai khoan", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(reg_message, textvariable=uname).pack()
    Label(reg_message, text="Mat khau", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(reg_message, textvariable=pw, show="*").pack()
    Button(reg_message, text="Dang ky", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=register).pack()

def logged_destroy():
    logged_message.destroy()
    root2.destroy()
 
def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message
    logged_message = Toplevel(root2)
    logged_message.title("Chao mung")
    logged_message.geometry("500x100")
    Label(logged_message, text="Dang nhap thanh cong!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Dang xuat", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=logged_destroy).pack()
 
def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Loi")
    failed_message.geometry("500x100")
    Label(failed_message, text="Tai khoan hoac mat khau khong dung!", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="OK", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=failed_destroy).pack()
 
def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from users where name = %s and hash = %s"
    cursordb.executemany(sql,[(user_verification),(pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
        else:
            failed()

def register():
    user_name = uname.get()
    pass_word = pw.get()
    sql = "insert into users (name, hash) values (%s, %s)"
    cursordb.executemany(sql, [(user_name, pass_word)])
    results = cursordb.fetchone()
    if results:
        for i in results:
            logged()
            break
        else:
            failed()
 
def Exit():
    wayOut = tkinter.messagebox.askyesno("Dang nhap", "Ban co muon thoat khong?")
    if wayOut > 0:
        root.destroy()
        return
 
def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Dang nhap")
    root.geometry("500x500")
    Label(root,text='Chao mung den voi he thong dang nhap', bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
    bg="blue",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Dang nhap', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white", bg="blue",command=login).pack()
    Label(root,text="").pack()
    Button(root, text='Dang ky', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white", bg="blue", command=register_screen).pack()
    Label(root, text="").pack()
    Button(root,text='Thoat', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white", bg="blue",command=Exit).pack()
    Label(root,text="").pack()

main_display()
root.mainloop()
