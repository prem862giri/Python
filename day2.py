a = 1 
'''

'''
print(type(a))

a = "true" 
print(type(a))

a= "sudan" 

print(type(a))

a = '1' 

print(type(a))

a = ''' 
this is my proiject
Hey'''
print(type(a))

a = None
print(type(a))

a = True
print(type(a))

a = ""
print(type(a))

a= 1.0 
print(type(a))

a = "prem"

a = "10"

print("Before Type Casting", type(a))

b = int(a)
print("After Type Casting ", type(b))

a = 10
print(isinstance(a,int))

a = 10
b = 2
print(a/b)

#floor Division
print(10//3)

#Modulus (Remainder)
print(10%3)

# Power
print(9**3)

# FOr string we can use + and *
print("Prem"+" Giri")
print("Prem"+ str(1))

print("Prem "* 10)

#Input function which is used to take data from users

# a = input(" Enter Your Value : ")
# print("User Entered : ", a, type(a))

# a = input("Enter a Number : ")
# b = input("Enter second Number : ")

# print(int(a)+ int(b))
# print("User Entered ", a, type(a))

fname = "Prem"
lname = "Giri"
age= 25
address = "Nepal"

print("My name is ",fname,"and last name is ",lname," age is ", age, " address is ",address)

print(f"My name is {fname} and last name is {lname} and age is {age}, address is {address}")