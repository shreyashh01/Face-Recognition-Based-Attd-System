from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recognition_System
from face_recognizor import Face_Recognition
import mysql.connector
import os
from student_details import Student
from train import Train
from attendance import Attendance
from developer import Developer
from time import strftime
from datetime import datetime
import tkinter


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\scene.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="light blue")
        frame.place(x=1110,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\login1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="light blue",borderwidth=0)
        lblimg1.place(x=1230,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times of new roman",17,"bold"),fg="black",bg="light blue")
        get_str.place(x=103,y=120)

        ########label

        username=lbl=Label(frame,text="Username",font=("times of new roman",15,"bold"),fg="black",bg="light blue")
        username.place(x=40,y=160)

        self.txtuser=ttk.Entry(frame,font=("times of new roman",15,"bold"))
        self.txtuser.place(x=40,y=185,width=270)


        password=lbl=Label(frame,text="password",font=("times of new roman",15,"bold"),fg="black",bg="light blue")
        password.place(x=40,y=230)

        self.txtpass=ttk.Entry(frame,font=("times of new roman",15,"bold"))
        self.txtpass.place(x=40,y=255,width=270)

        ###############ICON###################
        img2 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\login3.jpg")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="light blue", borderwidth=0)
        lblimg2.place(x=1120, y=360, width=25, height=25)

        img3 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\pass.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=1120, y=430, width=25, height=25)
#################login button
        loginbtn=Button(frame,command=self.login,text="LOGIN",font=("times of new roman",15,"bold"),bd=3,relief=RIDGE,fg="grey",bg="light blue",activeforeground="grey",activebackground="light blue")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #################reg buttion
        regbtn = Button(frame, text="Sign Up",command=self.register_window, font=("times of new roman", 10, "bold"), borderwidth=0, fg="black",
                          bg="light blue", activeforeground="light yellow", activebackground="black")
        regbtn.place(x=10, y=350, width=160)
        #######forgot passs
        forpassbtn = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times of new roman", 10, "bold"), borderwidth=0, fg="black",
                        bg="light blue", activeforeground="light yellow", activebackground="black")
        forpassbtn.place(x=20, y=390, width=160)


        #####################################

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        ##################################################



    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="123456789":
            messagebox.showinfo("Success","ACCESS GRANTED...")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="shreyash2002",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()

                                                                                   ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Admin Only")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
  #####################################resetoooo
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question")
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter your answer")
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="shreyash2002",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","please enter the correct answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, please login  with new password", parent=self.root2)
                self.root2.destroy()








#########################forrgorrr passs windewwwwwwwwww
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset the password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="shreyash2002",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("My Error","Please enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Passwrd",font=("times of new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                #######################row 3
                security_Q = Label(self.root2, text="Select Security Ques:", font=("times of new roman", 15, "bold"),
                                   fg="black",
                                   bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,
                                                     font=("times of new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth date", "your name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text=" security answers", font=("times of new roman", 15, "bold"), bg="white",
                                   fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2,
                                              font=("times of new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)
#############################################
                new_password = Label(self.root2, text="New password", font=("times of new roman", 15, "bold"),
                                   bg="white",
                                   fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2,
                                              font=("times of new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset", command=self.reset_pass, font=("times of new roman", 15, "bold"),fg="white",bg="green")
                btn.place(x=100,y=290)




                






class Register:
        def __init__(self, root):
            self.root = root
            self.root.title("Register")
            self.root.geometry("1600x900+0+0")

            ###############vairables
            self.var_fname = StringVar()
            self.var_lname = StringVar()
            self.var_contact = StringVar()
            self.var_email = StringVar()
            self.var_securityQ = StringVar()
            self.var_SecurityA = StringVar()
            self.var_pass = StringVar()
            self.var_confpass = StringVar()

            self.bg = ImageTk.PhotoImage(file=r"C:\\Users\\User\\Pycharm\\FACE_RECOGNITION\\clgimages\\wano1.jpg")

            bg_lbl = Label(self.root, image=self.bg)
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

            #################left image

            self.bg1 = ImageTk.PhotoImage(file=r"C:\\Users\\User\\Pycharm\\FACE_RECOGNITION\\clgimages\\merry.jpg")

            bg_lbl = Label(self.root, image=self.bg1)
            bg_lbl.place(x=50, y=100, width=470, height=550)
            ##############frame
            frame = Frame(self.root, bg="white")
            frame.place(x=520, y=100, width=800, height=550)

            register_lbl = Label(frame, text="Register Here", font=("times of new roman", 20, "bold"), fg="green",
                                 bg="white")
            register_lbl.place(x=20, y=20)

            ################entry row1
            fname_lbl = Label(frame, text=" First Name:", font=("times of new roman", 15, "bold"), fg="black",
                              bg="white")
            fname_lbl.place(x=50, y=100)

            self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times of new roman", 15, "bold"))
            self.fname_entry.place(x=50, y=130, width=250)

            l_name = Label(frame, text="last Name:", font=("times of new roman", 15, "bold"), fg="black", bg="white")
            l_name.place(x=370, y=100)

            self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times of new roman", 15, "bold"))
            self.txt_lname.place(x=370, y=130, width=250)

            #################row2
            contact = Label(frame, text="Contact No:", font=("times of new roman", 15, "bold"), fg="black", bg="white")
            contact.place(x=50, y=170)

            self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times of new roman", 15, "bold"))
            self.txt_contact.place(x=50, y=200, width=250)

            email = Label(frame, text="Email ID:", font=("times of new roman", 15, "bold"), fg="black", bg="white")
            email.place(x=370, y=170)

            self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times of new roman", 15, "bold"))
            self.txt_email.place(x=370, y=200, width=250)
#######################row 3
            security_Q = Label(frame, text="Select Security Ques:", font=("times of new roman", 15, "bold"), fg="black",
                               bg="white")
            security_Q.place(x=50, y=240)

            self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,
                                                 font=("times of new roman", 15, "bold"), state="readonly")
            self.combo_security_Q["values"] = ("Select", "Your Birth date", "your name")
            self.combo_security_Q.place(x=50, y=270, width=250)
            self.combo_security_Q.current(0)

            security_A = Label(frame, text=" security answers", font=("times of new roman", 15, "bold"), bg="white",
                               fg="black")
            security_A.place(x=370, y=240)

            self.txt_security = ttk.Entry(frame, textvariable=self.var_SecurityA,
                                          font=("times of new roman", 15, "bold"))
            self.txt_security.place(x=370, y=270, width=250)

            ##############row 4
            pswd = Label(frame, text="Password", font=("times of new roman", 15, "bold"), bg="white", fg="black")
            pswd.place(x=50, y=310)

            self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times of new roman", 15, "bold"))
            self.txt_pswd.place(x=50, y=340, width=250)

            confirm_pswd = Label(frame, text="Confirm Password", font=("times of new roman", 15, "bold"), bg="white",
                                 fg="black")
            confirm_pswd.place(x=370, y=310)

            self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass,
                                              font=("times of new roman", 15, "bold"))
            self.txt_confirm_pswd.place(x=370, y=340, width=250)

            #############################check button
            self.var_check = IntVar()
            checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree the Terms and Conditions",
                                   font=("times of new roman", 15, "bold"), onvalue=1, offvalue=0)
            checkbtn.place(x=50, y=380)

            ###############3333butttoooooooons###########
            img = Image.open(r"C:\\Users\\User\\Pycharm\\FACE_RECOGNITION\\clgimages\\reg1.png")
            img = img.resize((200, 50), Image.ANTIALIAS)
            self.photoimage = ImageTk.PhotoImage(img)
            b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2",
                        font=("times of new roman", 15, "bold"))
            b1.place(x=10, y=420, width=300)

            img1 = Image.open(r"C:\\Users\\User\\Pycharm\\FACE_RECOGNITION\\clgimages\\loginow.jpg")
            img1 = img1.resize((200, 50), Image.ANTIALIAS)
            self.photoimage1 = ImageTk.PhotoImage(img1)
            b1 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2",
                        font=("times of new roman", 15, "bold"))
            b1.place(x=330, y=420, width=300)

            #############fucn decl

        def register_data(self):
            if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
                messagebox.showerror("Error", "All fields required")
            elif self.var_pass.get() != self.var_confpass.get():
                messagebox.showerror("Error", "password and confirm password must be same")
            elif self.var_check.get() == 0:
                messagebox.showerror("Error", "Please agree  our terms and Condition")
            else:
                conn = mysql.connector.connect(host="localhost", username="root", password="shreyash2002",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                query = ("Select * from register where email=%s")
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User Already Exits,Please try another email")
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_SecurityA.get(),
                        self.var_pass.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", " Register Sucessfullly ")

        def return_login(self):
            self.root.destroy()

########################

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        ##first image
        img=Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\banner2.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #####second image
        img1 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\banner1.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        ####third image
        img2 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\face.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        ##bg image

        img3 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\background.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

         ###soft title
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM-ALSJ Bunts Sangha", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        ##########time##############
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(bg_img,font=('times of ew roman',13,'bold'),background='white',foreground='purple')
        lbl.place(x=0,y=80,width=110,height=40)
        time()


        ##buttons(student)
        img4 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\student.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.information,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text="Student Details",command=self.information, cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        ##button(detect face)
        img5 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\face_dectect.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        ###button(Attendance)
        img6 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\attd.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance)
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Take Attendance", cursor="hand2",command=self.attendance, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        ###button(train face)
        img7 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\train.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Facial Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

        ###button(photo)
        img8 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\gallery.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Gallery", cursor="hand2",command=self.open_img ,font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

        ###Developer
        img9 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\developer.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.developer)
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

        ##exit button
        img10 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\Exit.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.iExit)
        b1.place(x=1100, y=200, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1100, y=400, width=220, height=40)

    def open_img(self):
        os.startfile("data")

######+++++++++++++++++++++++++++fucntions to recallllllll+++++++++#################

    def information(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition ","Are You Sure You Wanna Exit?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()

        else:
            return





if __name__=="__main__":
    main()
