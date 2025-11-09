import tkinter as tk

import os
import cv2
import numpy as np
import time
import warnings 
from PIL import Image , ImageTk 
import matplotlib.image as mpimg
from playsound import playsound

warnings.filterwarnings("ignore", category=DeprecationWarning)
from keras.models import load_model
import emotion_1 as validate

#import CNNModel 

from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")

##############################################+=============================================================
image_x, image_y = 64, 64
basepath="E:/2024-2025 New Code/Music 100% code/music recommendation system/Images/dataset"

##############################################+=============================================================
root = tk.Tk()
root.configure(background="#ADD8E6")
root.geometry("1300x800")
root.title("Music Recommendation  System")
img = Image.open("E:/2024-2025 New Code/Music 100% code/music recommendation system/Images/m3.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((50, 50), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)
#####################################################+
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
image2 =Image.open('E:/2024-2025 New Code/Music 100% code/music recommendation system/Images/a3.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#


##########

label_l1 = tk.Label(root, text=" 'Music Recommendation Based on Face Emotion Recognition'",
                    font=("Times New Roman", 30, 'bold'),
                    background="#550A35", fg="#FFFFFF", height=1,width=55)
label_l1.place(x=0, y=10)

############################################


frame_CP = tk.LabelFrame(root, text="-------------- Control Panel ------------------", width=300, height=300, bd=5, font=('times', 12, ' bold '),
                         bg="#786D5F",fg="#000000")
frame_CP.grid(row=0, column=0, sticky='s')
frame_CP.place(x=10, y=80)


###################################################################################################################
def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=350, y=150)            
#################################################################################################################
def social():
           # from subprocess import call
        # call(['python','detection_emotion_practice.py'])
    validate.upload()
    prediction_emotion()
def prediction_emotion():
    #clear_img()
    #update_label("Model Training Start...............")

    start = time.time()

    result = validate.files_count()
    #validate.files_count()
    end = time.time()
    #print("---" + result)
    ET = "Execution Time: {0:.4} seconds \n".format(end - start)

    msg = "Model Training Completed.." + '\n' + str(result) + '\n'+ ET

    update_label(msg)  
    # if result=="Person is Happy.So this is the song for Him/Her":
    #     playsound('happy.mp3')
    # elif result=="Person is Neutral.So this is the song for Him/Her":
    #     playsound('neutral.mp3')
    # else:
    #     playsound('sad.mp3')
def prediction_emotion1():
    #clear_img()
    #update_label("Model Training Start...............")

    start = time.time()

    result = validate.files_count()
    #validate.files_count()
    # end = time.time()
    # #print("---" + result)
    # ET = "Execution Time: {0:.4} seconds \n".format(end - start)

    # msg = "Model Training Completed.." + '\n' + str(result) + '\n'+ ET

    # update_label(msg)  
    if result=="Person is Happy.So this is the song for Him/Her":
        playsound('E:/2024-2025 New Code/Music 100% code/music recommendation system/dataset/happy.mp3')
    elif result=="Person is Neutral.So this is the song for Him/Her":
        playsound('neutral.mp3')
    else:
        playsound('E:/2024-2025 New Code/Music 100% code/music recommendation system/dataset/sad.mp3')
        
def window():
    root.destroy()


button3 = tk.Button(frame_CP, text=" Face Emotions ", command=social,width=19, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button3.place(x=15, y=30)
button4 = tk.Button(frame_CP, text=" Recommend Music ", command=prediction_emotion1,width=19, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button4.place(x=15, y=100)

exit = tk.Button(frame_CP, text="Exit", command=window, width=19, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=15, y=170)



root.mainloop()