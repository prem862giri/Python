#College Admission
''' Input  :
--------------

Student's percentage
Entrance exam Score
Interview result(pass/fail)
'''

student_percent= float(input("Enter Student Percentage: "))

if student_percent>=60:
    entrance_score=float(input("Enter Your Entrance Exam Score: "))
    if entrance_score>=70:
        interview= bool(input("Enter Interview Result: "))
        if interview==True:
            print("admission is granted.")
        else:
            print("You Failed in interview")
    else:
        print("Your Entrance Exam Score is not meet criteria. ")
else:
    print("Your Percentage is not meet criteria")
