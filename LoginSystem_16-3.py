username="admine"
password="12345678"
secret_code="8526"
username1=str(input("enter user name:"))
password1=int(input("enter password"))
secret_code1=int(input("enter secret code"))
if username == username1 and password == password1 and secret_code == secret_code1:
    print("Welcome To Login Page..!!!")
elif username !=username1:
    print("username not found..")
elif password != password1:
    print("Incorrect Password..!")
elif secret_code != secret_code1:
    print("Wrong secret code..!")
else :
    print("Acess Denied !!")
