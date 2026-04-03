class Employee:
    def __init__(self,name,pno):
        self.name=name
        self.pno=pno
    def School(self):
        print("enter your name:",self.name,"enter your pno:",self.pno)
    def college(self):
        print("check your name:",self.name,"check your pno:",self.pno)
s1=Employee(name="guru",pno=34)
s1.School()
s1.college()