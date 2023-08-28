from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np





class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")


        ###soft title
        title_lbl = Label(self.root, text="Developer ",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="purple")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        ###############################################################################
        img_top = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\devlop2.jpg")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        img_top1 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\logo.jpg")
        img_top1 = img_top1.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=30, width=200, height=200)
################## developer info
        dev_label = Label(main_frame, text="Hey...We are Shreyash and Yashwardhan", font=("times of roman", 17, "bold"))
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="From ALSJ-Bunts Sangha", font=("times of roman", 17, "bold"))
        dev_label.place(x=0, y=40)

        dev_label = Label(main_frame, text="We are the developers", font=("times of roman", 17, "bold"))
        dev_label.place(x=0, y=75)

        dev_label = Label(main_frame, text="Of this system..)", font=("times of roman", 17, "bold"))
        dev_label.place(x=0, y=105)

        dev_label = Label(main_frame, text="for any query Email us on", font=("times of roman", 17, "bold"))
        dev_label.place(x=0, y=140)

        dev_label = Label(main_frame, text="naikshreyash01@gmail.com >", font=("times of roman", 17, "bold"))
        dev_label.place(x=0, y=175)

        dev_label = Label(main_frame, text="jaiswalyashwardhan724@gmail.com >", font=("times of roman", 17, "bold"))
        dev_label.place(x=0, y=215)
################img
        img2 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\we1.jpg")
        img2 = img2.resize((510, 390), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=255, width=510, height=390)

        ###############






if __name__ == "__main__":
    root = Tk()
    obj =Developer(root)
    root.mainloop()