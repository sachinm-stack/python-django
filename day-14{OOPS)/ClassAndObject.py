

class Student:
    def __init__(self,name,clas):
      self.name=name
      self.clas=clas
    
    def display(self):
       print("hi its me "+ (self.name) +"and My Age is"+str(self.clas))
       
s1= Student(name="koko",clas=12)
s2= Student(name="lolo",clas=15)
s3= Student(name="novo",clas=18)

s1.display()
s1.display()
s1.display()



