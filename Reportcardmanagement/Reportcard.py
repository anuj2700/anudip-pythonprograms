import mysql.connector
import random
#----------------------------------------------------------------------
class ReportCard:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost",user="root",passwd="123456",db="studentmanagement")
    #-------------------------------------------------------------------------------------
    # method to insert Studentdata
    def inputmarks(self,stdid,session,examtype,hin,eng,maths,sci,sst):
        #------------------------------------------------------------------------
        curobj=self.con.cursor()
        #datato insert
        rid = "result"+str(random.randint(200,5000))+stdid
        total = hin + eng + maths + sci + sst
        per = (total * 100)/500
        status=""
        if(hin>=35 and eng>=35 and maths >= 35 and sci >=35 and sst>=35 and per >= 35):
            status="pass"
        else: 
            status="fail"
        data = (rid,stdid,session,examtype,hin,eng,maths,sci,sst,total,per,status)
        #query to insert data into database
        querystring="insert into reportcard values('%s','%s','%s','%s',%d,%d,%d,%d,%d,%d,%d,'%s')"
        curobj.execute("insert into reportcard values('%s','%s','%s','%s',%d,%d,%d,%d,%d,%d,%d,'%s')"%(rid,stdid,session,examtype,hin,eng,maths,sci,sst,total,per,status))
        self.con.commit()
        x = curobj.rowcount
        self.con.close()
        return x
    #------------------------------------------------------------------------------------------
    #method to retrieve performance of student in a session
    def studentcurrentsessionperformance(self,stdid,session):
        #------------------------------------------------------------------------
        curobj=self.con.cursor()
        curobj.execute("Select examtype,percentage from reportcard where stdid = '%s' and session = '%s'"%(stdid,session))
        data = curobj.fetchall()
        self.con.close()
        return data
    #method to retrieve performance of student in a particular exam
    def studentcurrentexamperformance(self,stdid,session,examtype):
        #------------------------------------------------------------------------
        curobj=self.con.cursor()
        curobj.execute("Select hindi,english,maths,sci,sst from reportcard where stdid = '%s' and session = '%s' and examtype='%s'"%(stdid,session,examtype))
        data = curobj.fetchall()
        self.con.close()
        return data
    #---------------------------------------------------------------
    #method to retrieve subject wise performance of students in a sessionparticular exam
    def subjectwiseperformance(self,stdid,session,subject):
        #------------------------------------------------------------------------
        curobj=self.con.cursor()
        curobj.execute("Select examtype,%s from reportcard where stdid = '%s' and session = '%s'"%(subject,stdid,session))
        data = curobj.fetchall()
        self.con.close()
        return data
    