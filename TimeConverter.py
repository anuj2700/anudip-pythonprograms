#-------------------------------------------------------------
#program to convert seconds into equivalent hour minute and second
sec = int(input("Enter time(in second) : "))
print("------------------------------------")
hour = 0
min = 0
# conversion to hour
if(sec >= 3600):
    hour = sec // 3600
    sec = sec % 3600
# conversion to minute
if(sec >= 60):
    min = sec // 60
    sec = sec % 60
#----------------------------------------------------
print("Equivalent Time : ")
print(hour," Hour",min," Minute",sec," Second")
#-------------------------------------------------------------
