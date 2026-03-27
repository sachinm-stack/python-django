# print("hello world")
# name=input("wht is your name ? \n")
# college=input("eht is your clg ? \n")
# goal=input("wht is your goal ? \n")
# age=input("My age is ? \n")
# print("my name is "+ name + " and i going  to " + college + "and my goal is in life is" + goal + "and my age is"+age)






list1 = [10, 20, 30]
list2 = list1         # BUG: this is NOT a copy!

list2.append(99)

print(list1)   
print(list2)   
