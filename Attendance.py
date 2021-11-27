import tkinter.messagebox
import face_recognition
import imutils
import pickle
import time
import cv2
import os
import tkinter as tk
from pymongo import MongoClient
from tkinter import messagebox
import datetime


class Main:
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.arindam
    def __init__(self,regno,count):
        self.attendance(regno, count)



    def attendance(self, regno, count):
        if (count != 1):
            messagebox.showinfo("Information", "No Image or More than 1 Image Found Try Again")
        else:
            regno=regno[0]
            starttime = datetime.time(7, 30, 00)
            endtime = datetime.time(23, 0, 0)
            atAt = datetime.datetime.now()
            if atAt.time() < endtime and atAt.time() > starttime:
                # print("2nd Checkpoint")
                if ("Attendance" not in self.db.list_collection_names()):
                    atcol = self.db["Attendance"]


                if (self.exists(atAt,regno)):
                    self.UpdateDatabase(atAt,regno)
                else:
                    self.insertIntoDatabase(atAt, regno)
            else:
                messagebox.showinfo("Information","You reached Late or early")

    def exists(self,atAt,regno):

        sameDate=self.db.Attendance.find_one({"Date":"%s"%atAt.date()})
        # print(sameDate)
        if(sameDate==None):
            return False
        else:
            return True
    def UpdateDatabase(self,atAt,regno):
        regpref = regno[0:7]
        # print(regpref)
        RegPrefL = self.db.Attendance.find_one({"Date": "%s" % atAt.date()}, {"Daily.Registration Prefix": 1,"_id":0})
        RegPrefList=RegPrefL["Daily"]["Registration Prefix"]
        idToUpdate = self.db.Attendance.find_one({"Date": "%s" % atAt.date()}, {"_id": 1})
        if regpref in RegPrefList:
            studentSameRegPref = self.db.Attendance.find_one({"Date": "%s" % atAt.date(), }, {"Daily.%s"%regpref: 1})
            studentRegList=studentSameRegPref["Daily"]["%s"%regpref]
            if(regno in studentRegList):
                tk.messagebox.showinfo("Information","Attendance already taken")
            else:
                studentRegList.append(regno)
                self.db.Attendance.update_one({"_id": idToUpdate["_id"]},
                                              {"$set": {"%s" % regpref: studentRegList}})
                tk.messagebox.showinfo("Information", "Attendance taken %s"%regno)
        else:
            # update list and insert regpref
            RegPrefList.append(regpref)
            studList=[]
            studList.append(regno)
            self.db.Attendance.update_one({"_id": idToUpdate["_id"]}, {"$set": {"Daily.Registration Prefix": RegPrefList}})
            self.db.Attendance.update_one({"_id":idToUpdate["_id"]},{"$set":{"Daily.%s"%regpref:studList}})
            tk.messagebox.showinfo("Information", "Attendance taken %s" % regno)





    def insertIntoDatabase(self, atAt, regno):
        regpref = str(regno[0:7])
        # 1 For Present and 0 for absent by default
        list=[]
        list.append(regpref)
        l2=[]
        l2.append(regno)
        toadd = {'Year': "%s" % atAt.year,
                 "Date": "%s" % atAt.date(),
                 "WeekDay": "%s" % atAt.weekday(),
                 "Daily": {

                     "Registration Prefix": list,
                     "%s"%regpref:l2

                 }
                 }
        self.db.Attendance.insert_one(toadd)
        messagebox.showinfo("Information","Attendance Taken %s"%regno)
