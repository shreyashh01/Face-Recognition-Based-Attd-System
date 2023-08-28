from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np




mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")


        ########variables
        self.var_attend_id=StringVar()
        #self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()




        ##first image
        img = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\attd.png")
        img = img.resize((800, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        #####second image
        img1 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\attd2.jpg")
        img1 = img1.resize((800,200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        ##bg image

        img3 = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\attd3.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        ###soft title
        title_lbl = Label(bg_img, text="Attendance Management Details",
                          font=("times new roman", 35, "bold"),
                          bg="orange", fg="light blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        ##frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        ####left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                font=("times of roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"C:\Users\User\Pycharm\FACE_RECOGNITION\clgimages\attd4.png")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=370)

        ##########Lbel and entry
        #####id
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"))
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_id,
                                    font=("times new roman", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        ######ROLL
        #rolllabel = Label(left_inside_frame, text="Roll :", font=("times new roman", 12, "bold"))
        #rolllabel.grid(row=0, column=2, padx=4, pady=8)

        #atten_roll = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_roll,
                                       #font=("times new roman", 12, "bold"))
        #atten_roll.grid(row=0, column=3, pady=8)

        ##########Name
        namelabel = Label(left_inside_frame, text="Name :", font=("times new roman", 12, "bold"))
        namelabel.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_name,
                                       font=("times new roman", 12, "bold"))
        atten_name.grid(row=1, column=1,  pady=8)

        ####dep
        deplabel = Label(left_inside_frame, text="Department :", font=("times new roman", 12, "bold"))
        deplabel.grid(row=1, column=2,  pady=8)

        atten_dep = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_dep,
                                       font=("times new roman", 12, "bold"))
        atten_dep.grid(row=1, column=3,  pady=8)

        ######time
        timelabel = Label(left_inside_frame, text="Time :", font=("times new roman", 12, "bold"))
        timelabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_time,
                                       font=("times new roman", 12, "bold"))
        atten_time.grid(row=2, column=1, pady=8)

        ####date
        datelabel = Label(left_inside_frame, text="Date :", font=("times new roman", 12, "bold"))
        datelabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_date,
                                       font=("times new roman", 12, "bold"))
        atten_date.grid(row=2, column=3,  pady=8)

        ####attd
        attendancelabel = Label(left_inside_frame, text="Attendance :", font=("times new roman", 12, "bold"))
        attendancelabel.grid(row=3, column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_attend_attendance,font=("times new roman", 12),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        ##buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        save_btn = Button(btn_frame, text="Import cvs",command=self.importCsv, width=19, font=("times new roman", 12, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv",command=self.exportCsv, width=19,
                            font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update",  width=19, command=self.update_atten_status,
                            font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=19,command=self.reset_data,
                           font=("times new roman", 12, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)








        ####right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Database",
                                 font=("times of roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)

        #######scroll barsss
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        ##treeview
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        #self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"]="headings"


        self.AttendanceReportTable.column("id",width=100)
        #self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

################fetch data
    def fetechData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
######import csv
    def importCsv(self):
      global mydata
      mydata.clear()
      fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
      with open(fln) as myfile:
        csvread=csv.reader(myfile,delimiter=",")
        for i in csvread:
          mydata.append(i)
        self.fetechData(mydata)

            ####export data
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No  Data ","No Data Found",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open csv",
                                         filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data has been exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                  messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        #self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[1])
        self.var_attend_dep.set(rows[2])
        self.var_attend_time.set(rows[3])
        self.var_attend_date.set(rows[4])
        self.var_attend_attendance.set(rows[5])

        ####reset data

    def reset_data(self):
        self.var_attend_id.set("")
        #self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")

    #############################3
    def update_atten_status(self):
        new_status = self.var_attend_attendance.get()
        if new_status != "Status":
            self.atten_status.configure(values=("Status", "Present", "Absent"))
            self.atten_status.current(0)
            messagebox.showinfo("Success", "Attendance status updated.")
        else:
            messagebox.showerror("Error", "Please select a valid status.")




if __name__ == "__main__":
    root = Tk()
    obj =Attendance(root)
    root.mainloop()
