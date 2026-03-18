studMark=int(input("Enter the Student Mark:"))
if studMark >= 90:
    print("Grade: A ",studMark)
elif studMark >=75 and studMark < 90 :
    print("Grade: B ",studMark)
elif studMark >=40 and studMark < 75 :
    print("Grade: C ",studMark)
else:
    print("u got Fail Mark",studMark)