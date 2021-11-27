import datetime
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.arindam

cou="BAI"
doj="24/11/2021"
doj_dt=datetime.strptime(doj,'%d/%m/%Y')
print(doj_dt.year)
courseempty=db.Students.find({'Course Code':"%s"%cou,'Admission year':doj_dt.year}).count
print(courseempty   )
# a = "2020MIM10052"
# regpref = str(a[0:7])
# print(regpref)
# st = "%s" % atAt.date()
# list=["2020MIM10052"]

# toadd = {'Year': "%s" % atAt.year,
#          "Date": "%s" % atAt.date(),
#          "WeekDay": "%s" % atAt.weekday(),
#          "Daily":{
#
#              "Registration Prefix":"%s"%regpref,
#              "Present":list
#          }
#          }
# db.Attendance.insert_one(toadd)
# ls=["2020MIM10052","2020BCE10001"]
# y=db.Attendance.find_one({"Date":"%s"%atAt.date(),"Daily.Registration Prefix": "%s"%regpref}, {"Daily.Present": 1})
# print(y)
# print(y["_id"])
# print(y["Daily"]["Present"])
# db.Attendance.update_one({"_id":y["_id"]},{"$set":{"Daily.Present":ls}})

# NotSameRegPref=db.Attendance.find({"Date":"%s"%atAt.date()},{"Daily.Registration Prefix":1})
# couToday=[]
# for i in NotSameRegPref:
#     couToday.append(i["Daily"]["Registration Prefix"])

# sameDate=db.Attendance.find_one({"Date":"%s"%"2021-11-02"})
# print(sameDate
idToUpdate=db.Attendance.find_one({"Date": "%s" % doj_dt.date()},{"_id":1})
#
# print(idToUpdate)
# RegPrefList="BAI"
# studList=["2020MIM10052","2020MIM10001"]
# x=db.Attendance.find_one({"_id":idToUpdate["_id"]})
# print(x)
# db.Attendance.update_one({"_id": idToUpdate["_id"]},{"$set": {"Year": "2021"},"$set":{"Daily.Registration Prefix":"2020MIM"}})
#
# RegPrefL = db.Attendance.find_one({"Date": "%s" % doj_dt.date()}, {"Daily.Registration Prefix": 1,"_id":0})
# print(RegPrefL)
# print(RegPrefL["Daily"]["Registration Prefix"])
RegPrefList=["2020BAI"]
regpref="2020MIM"
st="Daily."+regpref
studentSameRegPref = db.Attendance.find_one({"Date": "%s" % doj_dt.date()}, {st: 1})
print(studentSameRegPref)