from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import numpy as np
import os

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #title bar
        title_lb=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),fg="red",bg="white")
        title_lb.place(x=0,y=0,width="1400",height="45")

        img_top=Image.open(r"college_images/facialrecognition.png")
        img_top=img_top.resize((1400,300),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f1=Label(self.root,image=self.photoimg_top)
        f1.place(x=0,y=55,width=1400,height=300)

        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),fg="black",bg="gold")
        b1_1.place(x=0,y=350,width=1400,height=60)

        img_bottom=Image.open(r"college_images/photo.jpg")
        img_bottom=img_bottom.resize((1400,300),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f1=Label(self.root,image=self.photoimg_bottom)
        f1.place(x=0,y=410,width=1400,height=300)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray Scale Image
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")



if __name__ == "__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()
