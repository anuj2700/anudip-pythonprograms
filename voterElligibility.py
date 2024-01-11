'''
Program to verify a person is elligible for voting or not
'''
age = int(input("Enter age (in year) : "))
if(age >= 18):
    print("Elligible for voting")
elif(age >= 0):
    print("Not elligible for voting")
else:
    print("Invalid Age")
