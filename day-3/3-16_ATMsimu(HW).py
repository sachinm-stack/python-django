pin=1234
balance=5000
pin1=int(input("enter the PIN Value"))
if pin == pin1:
    amount=int(input("enter the amount want "))
    if amount < 5000:
     print("successful withdraw the amount")
     print("balance money u have",balance-amount)
    else :
     print("insufficient Balance")
else:
  print("wrong pin")
