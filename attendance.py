from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import cv2
import os 
import csv
import numpy as np
from time import strftime

myData=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        img=Image.open(r"college_images/smart-attendance.jpg")
        img=img.resize((700,180),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f1=Label(self.root,image=self.photoimg)
        f1.place(x=0,y=0,width=700,height=180)

        img1=Image.open(r"college_images/students.jpg")
        img1=img1.resize((700,180),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f1=Label(self.root,image=self.photoimg1)
        f1.place(x=700,y=0,width=700,height=180)

        img3=Image.open(r"college_images/bgimg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg=Label(self.root,image=self.photoimg3)
        bg.place(x=0,y=180,width=1530,height=710)

        title_lb=Label(bg,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),fg="black",bg="silver")
        title_lb.place(x=0,y=0,width="1400",height="45")

        main_frame=Frame(bg,bd=2,bg="lightyellow")
        main_frame.place(x=10,y=55,width=1345,height=650)

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=670,height=485)

        img_left=Image.open(r"college_images/new1.png")
        img_left=img_left.resize((660,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f1=Label(left_frame,image=self.photoimg_left)
        f1.place(x=3,y=0,width=660,height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="lightyellow")
        left_inside_frame.place(x=0,y=135,width=665,height=292)

        attendanceId_label=Label(left_inside_frame,text="Attendance ID",font=("times new roman",12,"bold"),bg="lightyellow")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_id,width=22,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        rollLabel=Label(left_inside_frame,text="Roll No.",bg="lightyellow",font=("times new roman",12,"bold"))
        rollLabel.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_roll,width=22,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        nameLabel=Label(left_inside_frame,text="Name",bg="lightyellow",font=("times new roman",12,"bold"))
        nameLabel.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_name,width=22,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        depLabel=Label(left_inside_frame,text="Department",bg="lightyellow",font=("times new roman",12,"bold"))
        depLabel.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_dep,width=22,font=("times new roman",12,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        timeLabel=Label(left_inside_frame,text="Time",bg="lightyellow",font=("times new roman",12,"bold"))
        timeLabel.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_time,width=22,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        dateLabel=Label(left_inside_frame,text="Date",bg="lightyellow",font=("times new roman",12,"bold"))
        dateLabel.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_date,width=22,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        attendanceLabel=Label(left_inside_frame,text="Attendance Status",bg="lightyellow",font=("times new roman",12,"bold"))
        attendanceLabel.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        self.attend_status=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance,width=21,font=("times new roman",12,"bold"),state="readonly")
        self.attend_status["values"]=("Status","Present","Absent")
        self.attend_status.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        self.attend_status.current(0)

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="lightyellow")
        btn_frame.place(x=0,y=200,width=662,height=36)

        btn1=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        btn1.grid(row=4,column=0)

        btn2=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        btn2.grid(row=4,column=1)

        btn3=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        btn3.grid(row=4,column=2)

        btn4=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        btn4.grid(row=4,column=3)

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=690,y=10,width=640,height=485)

        tb_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="lightyellow")
        tb_frame.place(x=5,y=5,width=630,height=422)

        scroll_x=ttk.Scrollbar(tb_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tb_frame,orient=VERTICAL)

        self.AttendanceReport=ttk.Treeview(tb_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReport.xview)
        scroll_y.config(command=self.AttendanceReport.yview)

        self.AttendanceReport.heading("id",text="Attendance ID")
        self.AttendanceReport.heading("roll",text="Roll")
        self.AttendanceReport.heading("name",text="Name")
        self.AttendanceReport.heading("department",text="Department")
        self.AttendanceReport.heading("time",text="Time")
        self.AttendanceReport.heading("date",text="Date")
        self.AttendanceReport.heading("attendance",text="Attendance")

        self.AttendanceReport["show"]="headings"
        self.AttendanceReport.column("id",width=120)
        self.AttendanceReport.column("roll",width=120)
        self.AttendanceReport.column("name",width=120)
        self.AttendanceReport.column("department",width=120)
        self.AttendanceReport.column("time",width=120)
        self.AttendanceReport.column("date",width=120)
        self.AttendanceReport.column("attendance",width=120)
        self.AttendanceReport.pack(fill=BOTH,expand=1)
        self.AttendanceReport.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.AttendanceReport.delete(*self.AttendanceReport.get_children())
        for i in rows:
            self.AttendanceReport.insert("",END,values=i)

    def importCsv(self):
        global myData
        myData.clear()
        fl=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fl) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fl=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fl,mode="w",newline="") as myfile:
                ex_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    ex_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fl)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReport.focus()
        content=self.AttendanceReport.item(cursor_row)
        row=content['values']
        self.var_attend_id.set(row[0])
        self.var_attend_roll.set(row[1])
        self.var_attend_name.set(row[2])
        self.var_attend_dep.set(row[3])
        self.var_attend_time.set(row[4])
        self.var_attend_date.set(row[5])
        self.var_attend_attendance.set(row[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")



if __name__ == "__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()

