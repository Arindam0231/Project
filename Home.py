import tkinter as tk
import cv2
import tkcalendar
from tkinter import ttk
from PIL import Image, ImageTk
from pymongo import MongoClient
import pprint
from datetime import date
from datetime import datetime
import re
import os
import Registration
import Recognition
import requests
from io import BytesIO
from tkinter import messagebox
from ExtractingFace import extract

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        self.main()

    def main(self):
        frameopt=tk.Frame(self,width=int(w/2),height=h,bg="black")
        frameopt.pack(side="right")
        response = requests.get("https://cdn.pixabay.com/photo/2020/03/11/13/17/artificial-intelligence-4922134__340.jpg")
        bg = Image.open(BytesIO(response.content))
        bg = bg.resize((int(w / 2), h), Image.ANTIALIAS)
        frameopt.picbg = ImageTk.PhotoImage(master=frameopt, image=bg)
        lab = tk.Label(frameopt, image=frameopt.picbg)
        lab.place(x=0, y=0)
        headinglabel = tk.Label(frameopt, text="Automated Attendance System", font="Arial 30", bg="#ccffff", fg="black",
                                justify="center", pady=30, relief="solid")
        headinglabel.place(x=0, y=50,width=int(w/2))
        regbtn = tk.Button(frameopt, text="Register Student\n", font="Arial 20", bg="#ffffff", fg="#000000",
                           justify="center",
                           padx=30, pady=30)
        regbtn.bind("<Button>", lambda e: Registration.Registration())
        regbtn.place(x=80, y=200, relx=0.2,width=300)
        recbtn = tk.Button(frameopt, text="Take Attendance\n", font="Arial 20", bg="#ffffff", fg="#000000",
                           justify="center",
                           padx=30, pady=30)
        recbtn.bind("<Button>", lambda e: Recognition.Reco())
        recbtn.place(x=80, y=380, relx=0.2,width=300)
        recbtn = tk.Button(frameopt, text="Train Model\n", font="Arial 20", bg="#ffffff", fg="#000000",
                           justify="center",
                           padx=30, pady=30)
        recbtn.bind("<Button>", lambda e: extract())
        recbtn.place(x=80, y=560, relx=0.2,width=300)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Automated Attendance System")
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry("%dx%d" % (w, h))
    root.resizable(False,False)
    framepic=tk.Frame(root,width=int(w/2),height=h,bg="#0000cc")
    framepic.pack(side="left")

    frameapplogo = tk.Frame(framepic, width=int(w / 2), height=h,bg="#0000cc")
    frameapplogo.place(x=0, y=0)
    bg=Image.open("BackImg/bacckgroudapplogo2.jpg")
    bg = bg.resize((int(w / 2), h), Image.ANTIALIAS)
    frameapplogo.back = ImageTk.PhotoImage(master=frameapplogo, image=bg)
    lab = tk.Label(frameapplogo, image=frameapplogo.back)
    lab.place(x=0, y=0)

    bg = Image.open("BackImg/AppLogo.PNG")
    bg = bg.resize((200,200), Image.ANTIALIAS)
    frameapplogo.picbg = ImageTk.PhotoImage(master=frameapplogo, image=bg)
    lab = tk.Label(frameapplogo, image=frameapplogo.picbg)
    lab.place(x=20, y=60)
    appnamelabel=tk.Label(frameapplogo,text="On Time", font="Arial 56", fg="white",
                           justify="center",
                           padx=30, pady=30,bg="#002db3")
    appnamelabel.place(x=300,y=60,width=600)


    bg = Image.open("BackImg/VIT LOGO.png")
    bg = bg.resize((int(w / 2), int(h / 2)), Image.ANTIALIAS)
    frameapplogo.pic = ImageTk.PhotoImage(master=frameapplogo, image=bg)
    lab = tk.Label(frameapplogo, image=frameapplogo.pic)
    lab.place(x=0, y=0,rely=0.3)
    app = Application(master=root)
    app.mainloop()
