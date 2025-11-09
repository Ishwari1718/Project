# -*- coding: utf-8 -*-

########################Libraries Import######################################
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
import random
import re
###############################################################################

###################Window Setup################################################
root= tk.Tk()
root.geometry("1300x800")
root.title("REGISTRATION FORM")
root.configure(background="#ADD8E6")
img = Image.open("E:/2024-2025 New Code/Music 100% code/music recommendation system/Images/m3.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((50, 50), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)
###############################################################################

#######################frame###################################################
label = tk.Label(root, text="'Fill Up the Users Details'",font=("Times New Roman", 25, 'bold'),background="#FFAE42", fg="#FFFFFF", width=60, height=1)
label.place(x=300, y=0)

frame = tk.LabelFrame(root, text="Home", width=300, height=900, font=('times',18,'bold'),bg="#ADD8E6",fg="#000000")
frame.grid(row=0, column=0, sticky='nw')
frame.place(x=0, y=0)

def log():
    from subprocess import call
    call(["python","login.py"]) 
button1 = tk.Button(frame, text="Sign-In", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#0000FF", fg="#FFFFFF")
button1.place(x=0, y=80)  
    
  
def window():
    root.destroy()
button3 = tk.Button(frame, text="Logout",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="#000000", fg="#FFFFFF")
button3.place(x=0, y=150)
###############################################################################

##########################Database Connection##################################
Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()
value = random.randint(1, 1000)
print(value)

#database Connection code######################################################
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS music_users"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()
##### database connection done#################################################

##############password validation##############################################
def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 
##############password validation done#########################################

############# set a function to get user details from registration form########
def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM music_users WHERE username = ?')
    c.execute(find_user, [(username.get())])
    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation for correct enteries in form #
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO music_users(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))
            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            root.destroy()

###############################################################################



####labelization of registration form on window################################
l1 = tk.Label(root, text="Enter Your Name: ", width=20, font=("Times new roman", 20, "bold"), background="#FFAE42", fg="#FFFFFF")
l1.place(x=300, y=80)
t1 = tk.Entry(root, textvar=Fullname, width=30, font=('', 20))
t1.place(x=300, y=110)

l2 = tk.Label(root, text="Enter Your Address:", width=20, font=("Times new roman", 20, "bold"), background="#FFAE42", fg="#FFFFFF")
l2.place(x=300, y=150)
t2 = tk.Entry(root, textvar=address, width=30, font=('', 20))
t2.place(x=300, y=180)

l3 = tk.Label(root, text="Enter Your E-mail-ID:", width=20, font=("Times new roman", 20, "bold"), background="#FFAE42", fg="#FFFFFF")
l3.place(x=300, y=220)
t3 = tk.Entry(root, textvar=Email, width=30, font=('', 20))
t3.place(x=300, y=250)

l4 = tk.Label(root, text="Enter Your Phone-no:", width=20, font=("Times new roman", 20, "bold"), background="#FFAE42", fg="#FFFFFF")
l4.place(x=300, y=290)
t4 = tk.Entry(root, textvar=Phoneno, width=30, font=('', 20))
t4.place(x=300, y=320)

l5 = tk.Label(root, text="Enter Your Gender:", width=20, font=("Times new roman", 20, "bold"), background="#FFAE42", fg="#FFFFFF")
l5.place(x=300, y=360)
tk.Radiobutton(root, text="MALE", padx=5, width=5, bg="#ADD8E6", font=("times", 20), variable=var, value=1).place(x=650, y=360)
tk.Radiobutton(root, text="FEMALE", padx=20, width=4, bg="#ADD8E6", font=("times", 20), variable=var, value=2).place(x=770, y=360)

l6 = tk.Label(root, text="Enter Your Age:", width=20, font=("Times new roman", 20, "bold"), background="#FFAE42", fg="#FFFFFF")
l6.place(x=300, y=400)
t6 = tk.Entry(root, textvar=age, width=7, font=('', 20))
t6.place(x=650, y=400)

l7 = tk.Label(root, text="Enter Your User-Name:", width=20, font=("Times new roman", 20, "bold"), background="#FFAE42", fg="#FFFFFF")
l7.place(x=300, y=440)
t7 = tk.Entry(root, textvar=username, width=30, font=('', 20))
t7.place(x=300, y=470)

l8 = tk.Label(root, text="Enter Your Password :", width=20, font=("Times new roman", 20, "bold"),background="#FFAE42", fg="#FFFFFF")
l8.place(x=300, y=510)
t8 = tk.Entry(root, textvar=password, width=30, font=('', 20), show="*")
t8.place(x=300, y=540)

l9 = tk.Label(root, text="Re-Confirm Password:", width=20, font=("Times new roman", 20, "bold"), background="#FFAE42", fg="#FFFFFF")
l9.place(x=300, y=580)
t9 = tk.Entry(root, textvar=password1, width=30, font=('', 20), show="*")
t9.place(x=300, y=610)

button = tk.Button(root, text="SUBMIT", bg="#008000",font=("times",20),fg="white", width=10, height=1, command=insert)
button.place(x=850, y=580)

root.mainloop()
