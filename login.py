from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recognition_System
import random
import time
import datetime
import mysql.connector

def main():
    win=Tk()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        img1= Image.open(r"college_images/2-AI-invades-automobile-industry-in-2019.jpeg")
        img1= img1.resize((1530,750),Image.ANTIALIAS)
        self.photoImg1= ImageTk.PhotoImage(img1)
        bg_lb1=Label(self.root,image=self.photoImg1)
        bg_lb1.place(x=0,y=0,width=1530,height=750)

        title_lb=Label(bg_lb1,text="SMART PRESENCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lb.place(x=0,y=119,width="1400",height="45")

        downtitle=Label(self.root,text="Note: Enter Valid Username and Password",font=("times new roman",35,"bold"),fg="red",bg="white")
        downtitle.place(x=0,y=660,width="1400",height="37")

        img2= Image.open(r"college_images/facial-recognition_0.jpg")
        img2= img2.resize((455,120),Image.ANTIALIAS)
        self.photoImg2= ImageTk.PhotoImage(img2)
        bg_lb2=Label(self.root,image=self.photoImg2)
        bg_lb2.place(x=0,y=0,width=455,height=120)

        img3= Image.open(r"college_images/face-recognition.png")
        img3= img3.resize((455,120),Image.ANTIALIAS)
        self.photoImg3= ImageTk.PhotoImage(img3)
        bg_lb3=Label(self.root,image=self.photoImg3)
        bg_lb3.place(x=455,y=0,width=455,height=120)

        img4= Image.open(r"college_images/smart-attendance.jpg")
        img4= img4.resize((455,120),Image.ANTIALIAS)
        self.photoImg4= ImageTk.PhotoImage(img4)
        bg_lb4=Label(self.root,image=self.photoImg4)
        bg_lb4.place(x=908,y=0,width=455,height=120)

        frame= Frame(self.root,bg="black")
        frame.place(x=500,y=185,width=340,height=410)

        img5= Image.open(r"college_images/LoginIconAppl.png")
        img5= img5.resize((90,90),Image.ANTIALIAS)
        self.photoImg5= ImageTk.PhotoImage(img5)
        bg_lb5=Label(self.root,image=self.photoImg5,bg="black",borderwidth=0)
        bg_lb5.place(x=630,y=187,width=90,height=90)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="white")
        get_str.place(x=100,y=95)

        username_lb=Label(frame,text="Username",font=("times new roman",12,"bold"),bg="black",fg="white")
        username_lb.place(x=40,y=140)

        self.txtuser=StringVar()
        self.txtpass=StringVar()

        txtuser=ttk.Entry(frame,textvariable=self.txtuser,font=("times new roman",15,"bold"))
        txtuser.place(x=40,y=165,width=270)

        password_lb=Label(frame,text="Password",font=("times new roman",12,"bold"),bg="black",fg="white")
        password_lb.place(x=40,y=195)

        txtpass=ttk.Entry(frame,textvariable=self.txtpass,font=("times new roman",15,"bold"))
        txtpass.place(x=40,y=220,width=270)

        img6= Image.open(r"college_images/LoginIconAppl.png")
        img6= img6.resize((25,25),Image.ANTIALIAS)
        self.photoImg6= ImageTk.PhotoImage(img6)
        bg_lb6=Label(self.root,image=self.photoImg6,bg="black",borderwidth=0)
        bg_lb6.place(x=620,y=323,width=25,height=25)

        img7= Image.open(r"college_images/lock-512.png")
        img7= img7.resize((25,25),Image.ANTIALIAS)
        self.photoImg7= ImageTk.PhotoImage(img7)
        bg_lb7=Label(self.root,image=self.photoImg7,bg="black",borderwidth=0)
        bg_lb7.place(x=620,y=380,width=25,height=25)

        btn_login=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),relief=RIDGE,bd=3,fg="white",bg="red",activeforeground="white",activebackground="red")
        btn_login.place(x=110,y=270,width=120,height=35)

        btn_register=Button(frame,text="Register New User",font=("times new roman",10,"bold"),relief=FLAT,command=self.register_window,highlightthickness=0,bg="black",fg="white")
        btn_register.place(x=18,y=320,width=115)

        btn_forgot=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),relief=FLAT,highlightthickness=0,bg="black",fg="white")
        btn_forgot.place(x=15,y=350,width=115)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Field Required")
        elif self.txtuser.get()=="swati" and self.txtpass.get()=="bittu@123":
            messagebox.showinfo("Success","Welcome to Smart Presence Management System")
        else:
            messagebox.showerror("Invalid","Invalid Username and Passsword")




if __name__ == "__main__":
    root=Tk()
    obj = Login_Window(root)
    root.mainloop()



