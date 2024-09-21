from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import numpy as np

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variable
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stu_id=StringVar()
        self.var_stu_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radiobtn1=StringVar()

        img=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/face-recognition.png")
        img=img.resize((460,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f1=Label(self.root,image=self.photoimg)
        f1.place(x=0,y=0,width=460,height=130)

        img1=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/smart-attendance.jpg")
        img1=img1.resize((460,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f1=Label(self.root,image=self.photoimg1)
        f1.place(x=460,y=0,width=460,height=130)

        img2=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/students.jpg")
        img2=img2.resize((460,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f1=Label(self.root,image=self.photoimg2)
        f1.place(x=920,y=0,width=460,height=130)

        img3=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/bgimg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg=Label(self.root,image=self.photoimg3)
        bg.place(x=0,y=130,width=1530,height=710)

        #title bar
        title_lb=Label(bg,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),fg="black",bg="gold")
        title_lb.place(x=0,y=0,width="1400",height="45")

        main_frame=Frame(bg,bd=2,bg="lightyellow")
        main_frame.place(x=10,y=55,width=1345,height=650)

        left_frame=LabelFrame(main_frame,bd=2,bg="powderblue",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=670,height=485)


        img_left=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/new1.png")
        img_left=img_left.resize((660,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f1=Label(left_frame,image=self.photoimg_left)
        f1.place(x=3,y=0,width=660,height=130)

        course_frame=LabelFrame(left_frame,bd=2,bg="powderblue",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        course_frame.place(x=5,y=135,width=650,height=105)

        dept_label=Label(course_frame,text="Department",font=("times new roman",12,"bold"),bg="powderblue")
        dept_label.grid(row=0,column=0,padx=10)

        dept_combo=ttk.Combobox(course_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),state="readonly",width=17)
        dept_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical","Biomedical","EC")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10)

        course_label=Label(course_frame,text="Course",font=("times new roman",12,"bold"),bg="powderblue")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","FE","SE","TE","BE","BTECH","ME","MTECH")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        year_label=Label(course_frame,text="Year",font=("times new roman",12,"bold"),bg="powderblue")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","First Year","Second Year","Third Year","Fourth Year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        semester_label=Label(course_frame,text="Semester",font=("times new roman",12,"bold"),bg="powderblue")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select Semester","Semester A","Semester B")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        student_frame=LabelFrame(left_frame,bd=2,bg="powderblue",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        student_frame.place(x=5,y=240,width=650,height=215)

        studentId_label=Label(student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="powderblue")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(student_frame,textvariable=self.var_stu_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        studentName_label=Label(student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="powderblue")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(student_frame,textvariable=self.var_stu_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)

        studentRoll_label=Label(student_frame,text="Student Roll No.",font=("times new roman",12,"bold"),bg="powderblue")
        studentRoll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentRoll_entry=ttk.Entry(student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        studentRoll_entry.grid(row=1,column=1,padx=10,sticky=W)

        gender_label=Label(student_frame,text="Gender",font=("times new roman",12,"bold"),bg="powderblue")
        gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        dob_label=Label(student_frame,text="DOB",font=("times new roman",12,"bold"),bg="powderblue")
        dob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,sticky=W)

        phone_label=Label(student_frame,text="Phone No.",font=("times new roman",12,"bold"),bg="powderblue")
        phone_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=2,column=3,padx=10,sticky=W)

        address_label=Label(student_frame,text="Address",font=("times new roman",12,"bold"),bg="powderblue")
        address_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=3,column=1,padx=10,sticky=W)

        teacher_label=Label(student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="powderblue")
        teacher_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=3,column=3,padx=10,sticky=W)

        
        radiobtn1=Radiobutton(student_frame,variable=self.var_radiobtn1,text="Take Photo Sample",value="Yes",bg="powderblue",font=("times new roman",10,"bold"))
        radiobtn1.grid(row=4,column=0)

        radiobtn2=Radiobutton(student_frame,variable=self.var_radiobtn1,text="No Photo Sample",value="No",bg="powderblue",font=("times new roman",10,"bold"))
        radiobtn2.grid(row=4,column=1)

        take_photo_btn=Button(student_frame,command=self.generate_dataset,text="Take Photo Sample",width=15,font=("times new roman",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=4,column=2)

        update_photo_btn=Button(student_frame,text="Update Photo Sample",width=15,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=4,column=3)

        btn1=Button(student_frame,text="Save",command=self.add_data,width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        btn1.grid(row=5,column=0,pady=2)

        btn2=Button(student_frame,text="Update",command=self.update_data,width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        btn2.grid(row=5,column=1,pady=2)

        btn3=Button(student_frame,text="Delete",command=self.delete_data,width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        btn3.grid(row=5,column=2,pady=2)

        btn4=Button(student_frame,text="Reset",command=self.reset_data,width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        btn4.grid(row=5,column=3,pady=2)

        right_frame=LabelFrame(main_frame,bd=2,bg="lightgrey",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        right_frame.place(x=700,y=10,width=630,height=485)

        img_right=Image.open(r"/home/swati/Desktop/Face_Recognition_System/college_images/student.jpg")
        img_right=img_right.resize((620,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f1=Label(right_frame,image=self.photoimg_right)
        f1.place(x=3,y=0,width=620,height=130)

        search_frame=LabelFrame(right_frame,bd=2,bg="lightgrey",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=140,width=615,height=60)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="lightgrey")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=17)
        search_combo["values"]=("Select","Roll_no","Phone-no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)

        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,pady=2,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,pady=2,padx=4)

        table_frame=Frame(right_frame,bd=2,bg="lightgrey",relief=RIDGE)
        table_frame.place(x=5,y=200,width=615,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","roll","gender","dob","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phone",text="Phone_No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #funtion
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Swati@123",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                self.var_dept.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_stu_id.get(),
                                                                                                self.var_stu_name.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radiobtn1.get()

                                                                                         ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    
    #fetch
    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Swati@123",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                data=my_cursor.fetchall()

                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                          self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()

    #get cursor
    def get_cursor(self,event=""):
                cursor_focus=self.student_table.focus()
                content=self.student_table.item(cursor_focus)
                data=content["values"]
                self.var_dept.set(data[0]),
                self.var_course.set(data[1]),
                self.var_year.set(data[2]),
                self.var_semester.set(data[3]),
                self.var_stu_id.set(data[4]),
                self.var_stu_name.set(data[5]),
                self.var_roll.set(data[6]),
                self.var_gender.set(data[7]),
                self.var_dob.set(data[8]),
                self.var_phone.set(data[9]),
                self.var_address.set(data[10]),
                self.var_teacher.set(data[11]),
                self.var_radiobtn1.set(data[12])  

    #update
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Swati@123",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    
                                                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_stu_name.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radiobtn1.get(),
                                                                                                                                                                                    self.var_stu_id.get()

                                                                                                                                                                                    ))
                else:
                     if not Update:
                          return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)             
    #delete
    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Student Delete Page","Do you want to delete",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Swati@123",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_stu_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                     if not Delete:
                          return
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)           
    #reset
    def reset_data(self):
         self.var_dept.set("Select Department")
         self.var_course.set("Select Course")
         self.var_year.set("Select Year")
         self.var_semester.set("Select Semester")
         self.var_stu_id.set("")
         self.var_stu_name.set("")
         self.var_roll.set("")
         self.var_gender.set("Select Gender")
         self.var_dob.set("")
         self.var_phone.set("")
         self.var_address.set("")
         self.var_teacher.set("")
         self.var_radiobtn1.set("")

    #generate dataset
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Swati@123",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                     id+=1
                my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_stu_name.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radiobtn1.get(),
                                                                                                                                                                                    self.var_stu_id.get()==id+1

                                                                                                                                                                                 ))
                conn.commit()
                self.fetch_data()
                conn.close()

                #load predifiend data on frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #Scaling factor=1.3, Minimum neighbour
                    for(x,y,w,h) in faces:
                         face_cropped=img[y:y+h,x:x+w]
                         return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                     ret,myframe=cap.read()
                     if face_cropped(myframe) is not None:
                         img_id+=1
                         face=cv2.resize(face_cropped(myframe),(500,500))
                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                         file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                         cv2.imwrite(file_name_path,face)
                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                         cv2.imshow("Cropped Face",face)
                     
                     if cv2.waitKey(1)==13 or int(img_id)==100:
                          break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                    

if __name__ == "__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()
