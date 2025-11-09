# -*- coding: utf-8 -*-

"""
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
root.title("LOGIN FORM")
root.configure(background="#ADD8E6")
img = Image.open("E:/2024-2025 New Code/Music 100% code/music recommendation system/Images/m3.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((50, 50), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)
###############################################################################

#######################frame###################################################
label = tk.Label(root, text="'Fill In the Users Details'",font=("Times New Roman", 25, 'bold'),background="#FFAE42", fg="#FFFFFF", width=60, height=1)
label.place(x=300, y=0)

frame = tk.LabelFrame(root, text="Home", width=300, height=900, font=('times',18,'bold'),bg="#ADD8E6",fg="#000000")
frame.grid(row=0, column=0, sticky='nw')
frame.place(x=0, y=0)

def reg():
    from subprocess import call
    call(["python","registration.py"])
button2 = tk.Button(frame, text="Sign-Up",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#0000FF", fg="#FFFFFF")
button2.place(x=0, y=80)  
    
  
def window():
    root.destroy()
button3 = tk.Button(frame, text="Logout",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="#000000", fg="#FFFFFF")
button3.place(x=0, y=150)
###############################################################################

########################frame1#################################################
frame1 = tk.LabelFrame(root, text="Project  Developed By", width=1200, height=200, font=('times',18,'bold'),bg="#ADD8E6")
frame1.grid(row=0, column=0, sticky='nw')
frame1.place(x=300, y=550)


l1 = tk.Label(frame1, text="Student Name", width=12, font=("Times new roman", 18, "bold"), background="#ADD8E6", fg="#000000")
l1.place(x=0, y=10)

l2 = tk.Label(frame1, text="Student Name", width=12, font=("Times new roman", 18, "bold"), background="#ADD8E6", fg="#000000")
l2.place(x=500, y=10)

l3 = tk.Label(frame1, text="Student Name", width=12, font=("Times new roman", 18, "bold"), background="#ADD8E6", fg="#000000")
l3.place(x=0, y=50)

l4 = tk.Label(frame1, text="Student Name", width=12, font=("Times new roman", 18, "bold"), background="#ADD8E6", fg="#000000")
l4.place(x=500, y=50)
###############################################################################

###################Database Connection and Login form setup####################
username = tk.StringVar()
password = tk.StringVar()

def login():
    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()
   
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS music_users"
                        "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM music_users WHERE username= ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()
         if result:
            msg = ""
            print(msg)
            ms.showinfo("message", "User  Verified")
            from subprocess import call
            call(["python","music_master.py"])
         else:
          ms.showerror('Unauthorised', 'Name Or Password Did Not Found')
          
l1 = tk.Label(root, text="Enter Your Name: ", width=20, font=("Times new roman", 20, "bold"), background="#FFAE42", fg="#FFFFFF")
l1.place(x=500, y=80)
t1 = tk.Entry(root, textvar=username, width=30, font=('', 20))
t1.place(x=500, y=110)

l8 = tk.Label(root, text="Enter Your Password :", width=20, font=("Times new roman", 20, "bold"),background="#FFAE42", fg="#FFFFFF")
l8.place(x=500, y=150)
t8 = tk.Entry(root, textvar=password, width=30, font=('', 20), show="*")
t8.place(x=500, y=190)

btn = tk.Button(root, text="LOGIN", bg="#008000",font=("times",20),fg="#FFFFFF", width=9, height=0, command = login)
btn.place(x=650, y=250)

root.mainloop()
