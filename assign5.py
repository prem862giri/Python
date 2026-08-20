# Login System
''' Create a simple login program'''
d_username="admin"
d_password= "12345"

username=input("Enter username: ")
password= input("Enter password: ")

if username==d_username:
    if password==d_password:
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")