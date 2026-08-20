''' Write a program that marks in 3 subjects'''

sub1=float(input("Enter First subject marks: "))
sub2=float(input("Enter Second subject marks: "))
sub3=float(input("Enter Third subject marks: "))

average= (sub1+sub2+sub3)/3

if average>=80:
    print("Distinction")
elif average>=60:
    print("First Division")
elif average>=40:
    print("Pass")
else:
    print("Fail")