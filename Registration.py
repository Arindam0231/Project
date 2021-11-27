import tkinter as tk
import cv2
import face_recognition
import tkcalendar
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from pymongo import MongoClient
import pprint
from datetime import date
from datetime import datetime
import re
import os






class RegisterStudent():
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.arindam

    def __init__(self):
        self.newwin = tk.Tk()
        self.newwin.title("Register Student")
        w = self.newwin.winfo_screenwidth()
        h = self.newwin.winfo_screenheight()
        self.newwin.geometry("%dx%d" % (w, h))
        self.newwin.resizable(False, False)
        self.cap = cv2.VideoCapture(0)
        self.face_classifier=None
        self.face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
        self.dir="/media/arindam/Study/study mat/SEM 3/Project/Images"
        self.get()

    def get(self):
        w = self.newwin.winfo_screenwidth()
        h = self.newwin.winfo_screenheight()
        framedb = tk.Frame(self.newwin, width=int(w / 2), height=h)
        framedb.pack(side="left")
        bg = Image.open("BackImg/bacckgroudapplogo2.jpg")
        bg = bg.resize((int(w / 2), h), Image.ANTIALIAS)
        framedb.back = ImageTk.PhotoImage(master=framedb, image=bg)
        lab = tk.Label(framedb, image=framedb.back)
        lab.place(x=0, y=0)
        framevid = tk.Frame(self.newwin, height=h, width=int(w / 2), bg="white", highlightthickness=2)
        framevid.pack(side="right")
        bg = Image.open("BackImg/bacckgroudapplogo2.jpg")
        bg = bg.resize((int(w / 2), h), Image.ANTIALIAS)
        framevid.picbg = ImageTk.PhotoImage(master=framevid, image=bg)
        lab = tk.Label(framevid, image=framevid.picbg)
        lab.place(x=0, y=0)


        intro = tk.Label(framedb, text="Student Details", anchor="center", padx=3, pady=3, font="Arial 26 bold",bg="white", width=25)
        intro.place(x=0, y=30,width=int(w/2))
        frameinp1=tk.Frame(framedb,height=50,width=650,bg="white",highlightthickness=2)
        frameinp1.place(x=20,y=100)
        namevar=tk.StringVar()
        getname_lab=tk.Label(frameinp1,text="Name : ",anchor="center",padx=3,pady=2,font="Arial 22 bold",bg="white")
        getname_lab.place(x=30,y=5,width=150)
        getname_inp=tk.Entry(frameinp1,textvariable=namevar)
        getname_inp.place(x=200,y=10,height=30,width=400)

        frameinp2 = tk.Frame(framedb, height=50, width=650, bg="white",highlightthickness=2)
        frameinp2.place(x=20, y=160)
        getdob_lab = tk.Label(frameinp2, text="DOB : ", anchor="center", padx=3, pady=2, font="Arial 22 bold",bg="white")
        getdob_lab.place(x=30, y=5, width=150)
        getdob_inp = tkcalendar.DateEntry(frameinp2,font="Arial 16 ",state="readonly",date_pattern='dd/mm/y')
        getdob_inp.place(x=200, y=10, height=30, width=400)

        frameinp3 = tk.Frame(framedb, height=50, width=650, bg="white", highlightthickness=2)
        frameinp3.place(x=20, y=220)
        getgen_lab = tk.Label(frameinp3, text="Gender : ", anchor="center", padx=3, pady=2, font="Arial 22 bold",
                              bg="white")
        getgen_lab.place(x=30, y=5, width=150)
        gen=tk.StringVar()
        getgen_inp = ttk.Combobox(frameinp3, font="Arial 16 ", textvariable=gen, state="readonly")
        getgen_inp['values'] = ("Male", "Female","Others")
        getgen_inp.place(x=280, y=10, height=30)


        frameinp4 = tk.Frame(framedb, height=50, width=650, bg="white", highlightthickness=2)
        frameinp4.place(x=20, y=280)
        getphone_lab = tk.Label(frameinp4, text="Phone : ", anchor="center", padx=2, pady=2, font="Arial 22 bold",
                               bg="white")
        getphone_lab.place(x=30, y=5, width=150)
        getphone_inp = tk.Entry(frameinp4, font="Arial 16 ")
        getphone_inp.place(x=200, y=10, height=30, width=400)

        frameinp5 = tk.Frame(framedb, height=50, width=650, bg="white", highlightthickness=2)
        frameinp5.place(x=20, y=340)
        cou=tk.StringVar()
        getcou_lab = tk.Label(frameinp5, text="Course Code : ", anchor="center", padx=3, pady=2, font="Arial 22 bold",
                                bg="white")
        getcou_lab.place(x=30, y=5, width=210)
        getcou_inp = ttk.Combobox(frameinp5,font="Arial 16 ",textvariable=cou,state="readonly")
        CourseIds=self.db.Course.find({}, {"Course Code": 1, "_id": 0})
        temp=[]
        for i in CourseIds:
            if (i["Course Code"] not in temp):
                temp.append(i["Course Code"])

        getcou_inp['values']=tuple(temp)
        getcou_inp.place(x=280, y=10, height=30)

        frameinp8 = tk.Frame(framevid, height=50, width=800, bg="white", highlightthickness=2)
        frameinp8.place(x=20, y=100)
        getdoj_lab = tk.Label(frameinp8, text="Admission Date : ", anchor="center", padx=3,pady=1, font="Arial 22 bold",
                              bg="white")
        getdoj_lab.place(x=40, y=5, width=250)
        getdoj_inp = tkcalendar.DateEntry(frameinp8, font="Arial 16 ", state="readonly",date_pattern='dd/mm/y')
        getdoj_inp.place(x=350, y=10, height=30, width=400)

        frameinp9 = tk.Frame(framevid, height=50, width=800, bg="white", highlightthickness=2)
        frameinp9.place(x=20, y=160)
        getaad_lab = tk.Label(frameinp9, text="Aadhar Number : ", anchor="center", padx=3, pady=1, font="Arial 22 bold",
                              bg="white")
        getaad_lab.place(x=40, y=5, width=250)
        getaad_inp = tk.Entry(frameinp9, font="Arial 16 ")
        getaad_inp.place(x=400, y=10, height=30, width=300)

        frameinp10 = tk.Frame(framevid, height=50, width=800, bg="white", highlightthickness=2)
        frameinp10.place(x=20, y=220)
        getpas_lab = tk.Label(frameinp10, text="Passport Number : ", anchor="center", padx=3, pady=1, font="Arial 22 bold",
                              bg="white")
        getpas_lab.place(x=30, y=5, width=270)
        getpas_inp = tk.Entry(frameinp10, font="Arial 16 ")
        getpas_inp.place(x=400, y=10, height=30, width=300)

        frameinp7= tk.Frame(framedb, height=150, width=650, bg="white", highlightthickness=2)
        frameinp7.place(x=20, y=400)
        sub_btn=tk.Button(frameinp7, text="Show Subjects", font="Arial 20", bg="#ffffff", fg="#000000",justify="center",padx=5, pady=5)
        sub_btn.bind("<Button>", lambda e: self.showsub(framedb,framevid,getname_inp.get(),getdob_inp.get(),getgen_inp.get(),getphone_inp.get(),getcou_inp.get(),getdoj_inp.get(),getaad_inp.get(),getpas_inp.get()))
        sub_btn.place(x=30,y=20,width=200,height=70)


    def getRegistraion(self,name,dob,gen,pho,cou,doj,aad,pas):
        empty=self.db.Students.find()
        courseempty=self.db.Students.find_one({'Course Code':"%s"%cou,'Admission year':doj.year})
        max=0

        if (empty!=None or courseempty!=None):
            allreg=self.db.Students.find({'Course Code':cou},{'Registration Number':1,'_id':0})
            for y in allreg:
                exreg=y['Registration Number']
                x = int(exreg[7:])
                if(x>max):
                    max=x
        if (empty == None):
            max = 9999
        if (courseempty == None):
            max = 9999


        yrjoin=doj.year
        st=str(str(yrjoin)+cou+str(max+1))
        return st


    def showsub(self,framedb,framevid,name,dob,gen,pho,cou,doj,aad,pas):
        # Error handling in input
        if (aad=="" and pas==""):
            tk.messagebox.showerror("Error","Both Aadhar and Passport Field cannot remain empty")
            return
        nametrue=bool(re.match('[a-zA-Z\s]+$',name))
        phonetrue=bool(pho.isdigit() and len(pho)==10)
        passtrue=bool((re.match('[a-zA-z0-9\s]+$',pas) and len(pas)==9) or pas=="")
        aadtrue=bool((aad.isdigit() and len(aad)==12) or aad=="")
        dob_dt = datetime.strptime(dob, '%d/%m/%Y')
        cure = datetime.combine(date.today(), datetime.min.time())
        difference = cure-dob_dt
        diffyr = int((difference.days) / 365.2425)
        agetrue=bool(diffyr>=18)
        doj_dt=datetime.strptime(doj,'%d/%m/%Y')
        if(nametrue==False):
            tk.messagebox.showerror("Error","Name must consist only Alphabets")
            return
        if(phonetrue==False):
            tk.messagebox.showerror("Error","Phone Number must be of 10 digits")
            return
        if(passtrue==False):
            tk.messagebox.showerror("Error","Passport Number is wrong")
            return
        if(aadtrue==False):
            tk.messagebox.showerror("Error","Aadhar Number is should be of 12 Digits")
            return
        if(agetrue==False):
            tk.messagebox.showerror("Error","Student is under 17")
            return
        # if everythng works
        frameinp6=tk.Frame(framedb,height=250,width=650,bg="white",highlightthickness=2)
        frameinp6.place(x=20,y=560)
        u = tk.StringVar()
        x = self.db.Course.find({"Course Code": "%s" % cou, "Year": "%s" % doj_dt.year})
        st = ""
        for i in x:
            for o in i["Subject"]:
                st += "%s" % o + "\n"
        u.set(st)
        subdis_lab = tk.Label(frameinp6, text=u.get(), anchor="center", font="Arial 22 bold",
                              bg="white")
        subdis_lab.place(x=30,y=15, width=400,height=180)
        #Check is student already exists
        aadpadd=self.db.Students.find({},{'Aadhar Number':1,'Passport Number':1,'_id':0})
        similar=False
        for c in aadpadd:
            if((c['Aadhar Number']==aad and aad!="") or (c['Passport Number']==pas and pas!="") ):
                similar=True
        if(similar==True):
            tk.messagebox.showerror("Error","Student with same Aadhar or Passport Number exists")
        # To show Registration Number
        regNo=self.getRegistraion(name,dob,gen,pho,cou,doj_dt,aad,pas)

        # Insert into Student collection

        upl_sp=tk.Button(framevid,text="Upload Sample ",font="Arial 40",bg="white",justify="center",padx=3,pady=2)
        upl_sp.bind("<Button>",lambda e:self.database(framedb,framevid,regNo,name,dob,gen,pho,cou,doj,aad,pas))
        upl_sp.place(relx=0.3,rely=0.6,width=400,height=200)


    def database(self,framedb,framevid,regNo,name,dob,gen,pho,cou,doj,aad,pas):
        dob_dt = datetime.strptime(dob, '%d/%m/%Y')
        doj_dt = datetime.strptime(doj, '%d/%m/%Y')
        doy=doj_dt.year
        toadd = {'Registration Number': regNo, 'Course Code': cou, 'Name': name, 'Aadhar Number': aad,
                 'Passport Number': pas, 'Admission Date': doj_dt,'Admission year':doy, 'DOB': dob_dt, 'Gender': gen}
        self.db.Students.insert(toadd)
        framedb.pack_forget()
        framevid.pack_forget()
        self.camera(framedb,framevid,regNo,name,dob,gen,pho,cou,doj,aad,pas)

    def getfaceclassifier(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = self.face_classifier.detectMultiScale(gray, scaleFactor=1.1,
                                                     minNeighbors=5, minSize=(60, 60), flags=cv2.CASCADE_SCALE_IMAGE)
        for (x, y, w, h) in face:
            facecut = face[y:y + h, x:x + w]
            return facecut

    def getfacehog(self,frame):
        boxes = face_recognition.face_locations(frame, model='hog')
        if (boxes == []):
            return []
        else:
            for x, y, w, h in boxes:
                face = frame[x:w, h:y]
                return face
    def camera(self,framedb,framevid,regNo,name,dob,gen,pho,cou,doj,aad,pas):
        w = int(self.newwin.winfo_screenwidth() / 3)
        h = self.newwin.winfo_screenheight()
        imageId = 0
        while True:
            ret, pic = self.cap.read()
            face = self.getfacehog(pic)
            false = 0
            if (len(face) == 0):
                false = 1
            else:
                imageId += 1
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                face = cv2.resize(face, dsize=(200, 200), interpolation=cv2.INTER_CUBIC)
                cv2.imshow('Images', face)
                dname = self.dir + "/"+regNo
                if not os.path.exists(dname):
                    os.mkdir(dname)
                # Code to get and upload encodings in mongdb
                path = dname + "/" + regNo + "_" + str(imageId) + ".jpeg"
                cv2.imwrite(path, face)
                cv2.moveWindow('Images', int(self.newwin.winfo_screenwidth() / 3), 10)
                cv2.resizeWindow('Images', int(self.newwin.winfo_screenwidth() / 3), self.newwin.winfo_screenheight())
            if (cv2.waitKey(1) == ord('q') or int(imageId) == 100):
                break
        self.cap.release()
        cv2.destroyAllWindows()
        self.quit(framedb,framevid,path,regNo,name,dob,gen,pho,cou,doj,aad,pas)
        # code to get encodings from cropped face and sav in mongodb


    def quit(self,framedb,framevid,path,regNo,name,dob,gen,pho,cou,doj,aad,pas):
        #Get train the model
        tk.messagebox.showinfo("Information","Students Details Saved")
        self.newwin.quit()


def Registration():
    a=RegisterStudent()
    a.newwin.mainloop()
    a.quit()
#
# Registration()
