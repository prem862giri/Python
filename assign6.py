# Driving Licence Eligibility
''' Input:
age
citizenship status

Display an appropriate message for each situation'''

age = int(input("Enter Age : "))
citizenship= input("Enter Citizenship Status: ")

if age>=18:
    if citizenship=="Nepal" or citizenship=="nepal":
        print("You are Eligible for Licence. ")
    else:
        print("You are Foreigner.")
else:
    print("You are Minor")
