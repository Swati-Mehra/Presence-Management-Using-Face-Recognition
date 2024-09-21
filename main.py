from time import strftime
from datetime import datetime
from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os
import webbrowser

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #header
        img=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/b3.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f1=Label(self.root,image=self.photoimg)
        f1.place(x=0,y=0,width=500,height=130)

        img1=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f1=Label(self.root,image=self.photoimg1)
        f1.place(x=500,y=0,width=500,height=130)

        img2=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/b2.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f1=Label(self.root,image=self.photoimg2)
        f1.place(x=1000,y=0,width=500,height=130)

        img3=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/bg3.png")
        img3=img3.resize((1630,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg=Label(self.root,image=self.photoimg3)
        bg.place(x=0,y=130,width=1530,height=710)

        #title bar
        title_lb=Label(bg,text="SMART PRESENCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lb.place(x=0,y=125,width="1400",height="45")

        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text=string)
            lb1.after(1000,time)


        lb1= Label(title_lb,font=("times new roman",20,"bold"),background="gold",foreground="black")
        lb1.place(x=0,y=0,width=145,height=50)
        time()

        #student button
        img4=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/student.jpg")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=250,width=150,height=150)

        b1_1=Button(bg,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),fg="black",bg="gold")
        b1_1.place(x=100,y=370,width=150,height=40)

        #face detector button
        img5=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/face_detector1.jpg")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=300,y=250,width=150,height=150)

        b1_1=Button(bg,text="Mark Presence",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),fg="black",bg="gold")
        b1_1.place(x=300,y=370,width=150,height=40)

        #attendence face button
        img6=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/attendance.jpeg")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=500,y=250,width=150,height=150)

        b1_1=Button(bg,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),fg="black",bg="gold")
        b1_1.place(x=500,y=370,width=150,height=40)

        #train data button
        img7=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/Train.jpg")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg,image=self.photoimg7,command=self.train_data,cursor="hand2")
        b1.place(x=100,y=420,width=150,height=150)

        b1_1=Button(bg,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),fg="black",bg="gold")
        b1_1.place(x=100,y=530,width=150,height=40)

        #photos button
        img8=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/photo.jpg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg,image=self.photoimg8,command=self.open_img,cursor="hand2")
        b1.place(x=300,y=420,width=150,height=150)

        b1_1=Button(bg,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),fg="black",bg="gold")
        b1_1.place(x=300,y=530,width=150,height=40)

        #Exit button
        img9=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/exit.jpg")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg,image=self.photoimg9,command=self.exitt,cursor="hand2")
        b1.place(x=500,y=420,width=150,height=150)

        b1_1=Button(bg,text="Exit",command=self.exitt,cursor="hand2",font=("times new roman",15,"bold"),fg="black",bg="gold")
        b1_1.place(x=500,y=530,width=150,height=40)
    
    def open_img(self):
        #os.startfile('/home/swati/Desktop/Face_Recognition_System/data')
        webbrowser.open(os.path.realpath('/home/swati/Desktop/Face_Recognition_System/data'))
        #os.path.realpath('/home/swati/Desktop/Face_Recognition_System/data')
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def exitt(self):
        self.exitt= messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.exitt >0:
            self.root.destroy()
        else:
            return
            



if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()