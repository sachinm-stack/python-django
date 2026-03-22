# Q8. Smart Grade & Category System


marks = int(input('Enter marks (0-100): '))
# Validation
if marks < 0 or marks > 100:
 print('Invalid marks')
elif marks >90 and marks < 100:
 print("Grade A")
 print("Destinction")
 print("'Outstanding! Keep it up!'")
elif marks >75 and marks < 89:
 print("Grade B")
 print("Merit")
 print("'Outstanding! Keep it up!'")
elif marks >60 and marks <74:
 print("Grade C")
 print("Pass")
 print("'Outstanding! Keep it up!'")
elif marks >45 and marks <59:
 print("Grade D")
 print("Pass")
 print("'Outstanding! Keep it up!'")
elif marks <45:
 print("Fail")
 print("'Don't give up! Practice more.'")
else:
 print("try again")
