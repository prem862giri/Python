''' COMPARING OPERATOR'''
# print(2 == "2")
# print(2!=2)

# print("Hari" == "hari")
# print(5<2)


a = 6
b = 10
print(a == b)
print(a!=b)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)



''' LOGICAL OPERATOR'''
print(True and True)
print(False or True)
print(not(True))


print(2==2 and True)

print(5>2 and 10<0)





''' IF CONDITION'''

a = 2
if (a == 4):
    print("This is testing")

if (2==4):
    print("True Condition")
    print("Code Block of if condition")

else:
    print("This is else block")


# Example 1(Odd number and Even Number)
# a = int(input("Enter the number: "))
# if (a%2 == 0):
#     print(f"{a} number is Even")

# else:
#     print(f"{a} number is Odd")


if (1==1 and 2==2):
    print("If condition is if")
elif(1==3):
    print("This is elif condition")
elif(2==3):
    print("This is 2nd elif condition")
else:
    print("This is else")


#Exercise 2(Grade)
grade = float(input("Enter Your Grade: "))
if (grade<=4 and grade>3.6):
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
    print("Invalid Number")
