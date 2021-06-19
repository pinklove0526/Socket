from tkinter import *
import os
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Dang ky")
    register_screen.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Vui long nhap thong tin sau").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Tai khoan*")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Mat khau*")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Dang ky", width=10, height=1, command = register_user).pack()
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Dang nhap")
    login_screen.geometry("300x250")
    Label(login_screen, text="Vui long nhap thong tin sau de dang nhap").pack()
    Label(login_screen, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Tai khoan* ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Mat khau* ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Dang nhap", width=10, height=1, command = login_verify).pack()
 
def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(register_screen, text="Dang ky thanh cong!", fg="green", font=("calibri", 11)).pack()
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognized()
    else:
        user_not_found()
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Thanh cong")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Dang nhap thanh cong!").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
def password_not_recognized():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Loi")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Sai mat khau!").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognized).pack()
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Loi")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Khong tim thay nguoi dung!").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()
 
def delete_password_not_recognized():
    password_not_recog_screen.destroy()
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Dang nhap tai khoan")
    Label(text="Dang nhap hoac dang ky", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Dang nhap", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Dang ky", height="2", width="30", command=register).pack()
    main_screen.mainloop() 

main_account_screen()