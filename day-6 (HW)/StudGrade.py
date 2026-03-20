studmark={"sac":90,
          "Aru":95,
          "mar":100}
print(studmark.keys())
print(studmark.values())
print(studmark.items())
ename=str(input("enter stud name:"))
if ename in  studmark.keys():
    print(studmark[ename])
else:
    print("user name not found !")