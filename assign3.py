#Largest of Three numbers
''' Take three numbers as input and determine the largest number using only if-else conditions'''

num1=int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1>num2 and num1>num3:
    print(f"The largest number is number 1. i.e, {num1} ")
elif num2>num3:
    print(f"The largest number is number 2. i.e,  {num2}")
else:
    print(f"The largest number is number 3. i.e,  {num3}")