from tkinter import *
import os

def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.geometry("350x250")
    screen2.title("Login")
    
    global email_verify
    global username_verify
    global password_verify
    global email_entry_login
    global password_entry_login
    global username_entry_login

    email_verify=StringVar()
    username_verify=StringVar()
    password_verify=StringVar()

    Label(screen2,text="Please enter your details to login").pack()
    Label(screen2,text="").pack()
    
    Label(screen2,text="Email").pack()

    email_entry_login=Entry(screen2,textvariable=email_verify)
    email_entry_login.pack()
    
    Label(screen2,text="").pack()
    Label(screen2,text="Username").pack()
    username_entry_login=Entry(screen2,textvariable=username_verify)
    username_entry_login.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Password").pack()
    password_entry_login=Entry(screen2,textvariable=password_verify)
    password_entry_login.pack()
    Button(screen2,text="Login",width="20",height="3",command=login_verify).pack()

def login_verify():

    email_login_verification=email_verify.get()
    username_login_verification=username_verify.get()
    password_login_verification=password_verify.get()

    email_entry_login.delete(0,END)
    username_entry_login.delete(0,END)
    password_entry_login.delete(0,END)

    file_list=os.listdir()
    if username_login_verification in file_list:
        new_file=open(username_login_verification,"r")
        verify=new_file.read().splitlines()
        if email_login_verification in verify:
            print("email matched")
        else:
            print("email is not matched")
        if password_login_verification in verify:
            print("password matched")
        else:
            print("password is not matched")
    else:
        print("username is not found")
        
def registration_user():
    
    info_email=email.get()
    info_password=password.get()
    info_username=username.get()

    file=open(info_username,"w")
    file.write(info_email+"\n")
    file.write(info_password+'\n')
    file.close()

    email_entry.delete(0,END)
    password_entry.delete(0,END)
    username_entry.delete(0,END)

    Label(screen1,text="success!!",fg="green",font=("Calibri",14)).pack()
    
def register():
    
    
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("400x250")
    screen1.title("Registration Form")
    global email,username,password
    global email_entry
    global password_entry
    global username_entry
    email=StringVar()
    username=StringVar()
    password=StringVar()
    
    Label(screen1,text="email").pack()
    email_entry=Entry(screen1,textvariable=email)
    email_entry.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="username").pack()
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Password").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Button(screen1,text="YES ! i am sure, Register",width="20",height="3",command=registration_user).pack()


def main_interface():
     global screen
     screen=Tk()
     screen.geometry("650x450")
     screen.title("LOG IN PAGE")
     Label(text="Log in / Register", bg = "orange", width="40",height="5",font=("Arial",16)).pack()
     Label(text="").pack()
     Label(text="Please , Log in if you have an id").pack()
     Button(text="Log in",height="3",width="20",command=login).pack()
     Label(text="").pack()
     Label(text="Please , Do register").pack()
     Button(text="Register",height="3",width="20",command=register).pack()
     
     screen.mainloop()


main_interface()     
     

