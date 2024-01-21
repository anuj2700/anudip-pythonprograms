from Reportcard import *
from StudentData import *
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------
operation = True
while operation:
    print("-------------------------------------------------------------------")
    print("1. Register any student")
    print("2. Insert Marks of Student")
    print("3. Display Student Details")
    print("4. Display Overall performance in a session")
    print("5. Subject wise performance in a session")
    print("6. Performance in a particular exam")
    print("----------------------------------------------------------------------")
    data=int(input("Select any one operation : "))
    if(data == 1):
        #----------------------------------
        print("-------------------------------------------------------------")
        print("-----Student Details Entry-----------")
        stdid=input("Enter student id : ")
        stdname=input("Enter name : ")
        std=input("Enter standard : ")
        roll=int(input("Enter roll number : "))
        #creating student object
        std1=StudentData()
        i = std1.registerStudent(stdid,stdname,std,roll)
        if(i > 0):
            print("Student registration successfull")
        else:
            print("Unable to register the student")
    elif(data == 2):
        #----------------------------------------
        print("-------------------------------------------------------------")
        print("-----Marks Details Entry-----------")
        stdid=input("Enter student id : ")
        examtype=input("Enter exam type(Term 1 / Term 2 / Term 3 / Annual) : ")
        session=input("Enter session(e.g 2022-23) : ")
        hin = int(input("Enter marks of hindi : "))
        eng = int(input("Enter marks of english : "))
        maths = int(input("Enter marks of mathematics : "))
        sci = int(input("Enter marks of science : "))
        sst = int(input("Enter marks of social studies : "))
        #creating object of reportcard
        report = ReportCard()
        i = report.inputmarks(stdid,session,examtype,hin,eng,maths,sci,sst)
        if(i > 0):
            print("Markssheet Creation Successfull")
        else:
            print("Unable to create Marksheet")
    elif(data == 3):
        #----------------------------------------
        print("---------------------------------------------")
        stdid=input("Enter student id : ")
        #creating object of studentdata
        std1=StudentData()
        data = std1.retrieveStudentdata(stdid)
        if(len(data) > 0):
            print("Student id : ",data[0][0])
            print("Student Name : ",data[0][1])
            print("Standard : ",data[0][2])
            print("Roll No. : ",data[0][3])
        else:
            print("No record found")
    elif(data == 4):
        #----------------------------------------
        print("-----------------------------------------------------------")
        stdid = input("Enter student id : ")
        session = input("Enter session (e.g, 2022-23): ")
         #creating object of reportcard
        report = ReportCard()
        data = report.studentcurrentsessionperformance(stdid,session)
        if(len(data) > 0):
            x_values = []
            y_values = []
            for x in data:
                x_values.append(x[0])
                y_values.append(x[1])
            plt.bar(x_values, y_values, color='blue')
            # Add labels to the axes
            plt.xlabel('Examination Type')
            plt.ylabel('Percentage(in %)')

            # Add a title to the plot
            plt.title(' Session %s Performance'%(session))

            # Add a legend
            plt.legend()

            # Show the plot
            plt.show()
        else:
            print("No Data found")
    elif(data == 5):
        #----------------------------------------
        #----------------------------------------
        print("-----------------------------------------------------------")
        stdid = input("Enter student id : ")
        session = input("Enter session (e.g, 2022-23): ")
        sub=""
        print("Select subject : ")
        print("1. hindi")
        print("2. English")
        print("3. Maths")
        print("4. Science")
        print("5. Social Studies")
        x = int(input())
        if(x==1):
            sub="hindi"
        elif(x==2):
            sub="english"
        elif(x==3):
            sub = "maths"
        elif(x == 4):
            sub = "science"
        elif(x==5):
            sub="sst"
         #creating object of reportcard
        report = ReportCard()
        data = report.subjectwiseperformance(stdid,session,sub)
        if(len(data) > 0):
            
            x_values = []
            y_values = []
            for x in data:
                x_values.append(x[0])
                y_values.append(x[1])
            plt.bar(x_values, y_values, color='blue')
            # Add labels to the axes
            plt.xlabel('Examination Type')
            plt.ylabel('Percentage(in %)')

            # Add a title to the plot
            plt.title(' SUbject %s Performance'%(sub))

            # Add a legend
            plt.legend()

            # Show the plot
            plt.show()
        else:
            print("No Data found")
    elif(data == 6):
        #----------------------------------------
        print("-----------------------------------------------------------")
        stdid = input("Enter student id : ")
        session = input("Enter session (e.g, 2022-23): ")
        examtype=input("Enter exam type(Term 1 / Term 2 / Term 3 / Annual) :" )
         #creating object of reportcard
        report = ReportCard()
        data = report.studentcurrentexamperformance(stdid,session,examtype)
        if(len(data) > 0):
            x_values = ['Hindi','English','Maths','Science','Social Studies']
            y_values = [data[0][0],data[0][1],data[0][2],data[0][3],data[0][4]]
            for x in data:
                x_values.append(x[0])
                y_values.append(x[1])
            plt.bar(x_values, y_values, color='blue')
            # Add labels to the axes
            plt.xlabel('Subjects')
            plt.ylabel('Marks out of 100')

            # Add a title to the plot
            plt.title(' Session %s Performance'%(session))

            # Add a legend
            plt.legend()

            # Show the plot
            plt.show()
        else:
            print("No Data found")
    else:
        print("Invalid Selection")
    print("-----------------------------------------------------------------")
    ops=input("Insert Y to contiue or N to exit : ")
    print("------------------------------------------------------------------\n\n\n")
    if(ops=='N' or ops == 'n'):
        operation = False
    else:
        pass

