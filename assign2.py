#Electricity Bill
''' Input the number of electricity units consumed'''

units = int(input("Enter the used Units: "))
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