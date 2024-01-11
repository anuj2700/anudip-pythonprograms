#-------------------------------------------------------------
#program to check leap year
year = int(input("Enter any year : "))
print("------------------------------------")
if(year % 100 == 0):
    if(year % 400 == 0):
        print("Leap year")
    else:
        print("Not Leap year")
else:
    if( year % 4 == 0):
        print("Leap year")
    else:
        print("Not Leap year")
#-------------------------------------------------------------
