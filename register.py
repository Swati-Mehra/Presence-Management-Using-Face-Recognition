from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recognition_System
import random
import time
import datetime
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

if __name__ == "__main__":
    root=Tk()
    obj = Register(root)
    root.mainloop()