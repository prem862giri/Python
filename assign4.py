#Number Classification
''' Input an integer and determine whether it is: '''

num=int(input("Enter any number: "))

if num>0 and num%2==0:
    print("This is Positive even number. ")
elif num>0:
    print("This is Positive odd number. ")
elif num<0 and num%2==0:
    print("This is Negative even number. ")
elif num<0:
    print("This is Negative odd number. ")
else:
    print("This is Zero")