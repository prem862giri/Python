#ATM Withdrawal
''' 
INPUT    :
-------------

Account balance
Withdrawal amount
PIN
'''

d_pin=2222
balance=50000

pin=int(input("Enter Your PIN : "))

if pin==d_pin:
    withdraw=int(input("Enter Withdrawal amount: "))
    if withdraw<balance:
        rem_balance=balance-withdraw
        print("Your Transaction is completed.")
        print("Your remaining balance is ",rem_balance)
    else:
        print("Insufficient Balance")

    
else:
    print("Incorrect PIN")
