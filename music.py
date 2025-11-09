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
###############################################################################


###################Window Setup################################################
root = tk.Tk()
root.configure(background="#ADD8E6")
root.geometry("1300x800")
root.title("Music Recommendation  System")
img = Image.open("E:/2024-2025 New Code/Music 100% code/music recommendation system/Images/m3.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((50, 50), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)
###############################################################################

#############background image##################################################
image2 = Image.open('E:/2024-2025 New Code/Music 100% code/music recommendation system/Images/w1.jpg')
image2 = image2.resize((1200, 700), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=300, y=0)  # , relwidth=1, relheight=1)
###############################################################################

####################Label on Window############################################
label = tk.Label(root, text="'Music Recommendation Based on Face Emotion Recognition'",font=("Times New Roman", 25, 'bold'),background="#152238", fg="#FFFFFF", width=50, height=1)
label.place(x=300, y=0)
###############################################################################

##########################Frame################################################
frame = tk.LabelFrame(root, text=" --Home-- ", width=300, height=900, bd=5, font=('times', 14, ' bold '),bg="#040720",fg="#FFFFFF")
frame.grid(row=0, column=0, sticky='nw')
frame.place(x=0, y=0)


def reg():
    from subprocess import call
    call(["python","registration.py"])
button2 = tk.Button(frame, text="Sign-Up",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#008000", fg="#FFFFFF")
button2.place(x=0, y=140)

def log():
    from subprocess import call
    call(["python","login.py"]) 
button1 = tk.Button(frame, text="Sign-In", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#0000FF", fg="#FFFFFF")
button1.place(x=0, y=80)  
    
  
def window():
    root.destroy()
button3 = tk.Button(frame, text="Logout",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="#000000", fg="#FFFFFF")
button3.place(x=0, y=200)
###############################################################################
root.mainloop()
