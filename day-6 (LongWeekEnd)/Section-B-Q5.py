# Q5. Personal Details Program
# Write a program that asks the user for their name, age, city, and favourite programming language. Store each in a variable with the
# correct data type. Then print a properly formatted introduction sentence using string concatenation AND f-strings (do both).
# Take these inputs from the user:

name = input('Enter your name: ')
age = int(input('Enter your age: '))
city=input("enter your city: ")
Planguage=input("enter your favurite lang :")

# Method 1 — string concatenation using +

print("Hi,i am "+ name +"  name len i have "+str(len(name))+"  Age   "+str(age) +" 5 years later  "+str(age+5)+" from "+ city +"  and my favrite programming language is  " +Planguage)

# Method 2 — f-string

print(f"Hi,My Name Is { name } len of char name {len(name)} and My Age Is  {age} 5 years later{age+5} and i am from { city }  and my favrite programming language is  {Planguage}")
