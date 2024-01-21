import mysql.connector
import random
#----------------------------------------------------------------------
class StudentData:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost",user="root",passwd="123456",db="studentmanagement")
    #-------------------------------------------------------------------------------------
    # method to insert Studentdata
    def registerStudent(self,stdid,stdname,std,roll):
        #------------------------------------------------------------------------
        curobj=self.con.cursor()
        data = (stdid,stdname,std,roll)
        #query to insert data into database
        querystring="insert into studentdetails (stdid,stdname,std,roll)values(%s,%s,%s,%d)"
        curobj.execute("insert into studentdetails (stdid,stdname,std,roll)values('%s','%s','%s',%d)"%(stdid,stdname,std,roll))
        self.con.commit()
        x = curobj.rowcount
        self.con.close()
        return x
    #------------------------------------------------------------------------------------------
    #method to retrieve student details
    def retrieveStudentdata(self,stdid):
        #------------------------------------------------------------------------
        curobj=self.con.cursor()
        curobj.execute("Select * from studentdetails where stdid = '%s'"%(stdid))
        data = curobj.fetchall()
        self.con.close()
        return data