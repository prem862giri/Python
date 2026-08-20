''' Nested if'''

#grade = float(input("Enter Your Grade: "))
grade=4
if (grade<=4 and grade>3.6):
    if (grade ==4):
        print("Topper")
    print("A+")
elif(grade<=3.6 and grade>3.2):
    print("A")
elif(grade<=3.2 and grade>2.8):
    print("B+")
elif(grade<=2.8 and grade>2.4):
    print("B")
elif(grade<=2.4 and grade>2.0):
    print("C+")
elif(grade<=2.0 and grade>1.6):
    print("C")
elif(grade<=1.6 and grade>0):
    print("Fail")
else:
    if (grade>4.0):
     print("Invalid Number")
    elif (grade<0):
        print("Grade should be in Positive")
    else:
        print(f"{grade} is an Error GPA")




''' Single line'''

#Method 1
gender = "M"
if gender =="M":
    print("Male")
else:
    print("Female")

#Method 2(This is single line statement for if - else statement)
data = "Male" if gender =="M" else "Female"
print(data)



#Example 2:
number = 9
data = f"{number} is even" if number%2==0 else f"{number} is odd"
print(data)







# Practice 
'''Electricity bill

Upto 100 units--> Rs. 5 per unit
101 - 200 units --> Rs. 7 per units
201 - 300 units --> Rs. 10 per units
Above 300 units --> Rs. 12 per units
'''

#units = int(input("Enter the used Units: "))
units =200
if units<=100:
    amount = 5* units
    print(f"Your total bill is  Rs.{amount}")
elif units<=200:
    amount = 7 * units
    print(f"Your total bill is  Rs.{amount}")
elif units<=300:
    amount= 10 * units
    print(f"Your total bill is  Rs.{amount}")
else:
    if units<0:
        print("Unit should be positive")
    else:
        amount = 12 * units
        print(f"Your total bill is  Rs.{amount}")








# Practice 
''' Login System
create a simple login program

Input:
username
password

use nested if'''
user_name = "admin"
d_password= "12345"

username = input("Enter username: ")
print(username)
password = input("Enter Password")
print(password)


if username==user_name and password==d_password:
    print("Login Successful")
    
else:
    if password!= d_password:
        print("Incorrect Password")
    else:
        print("Invalid Username")