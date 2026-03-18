pin="1234"
balance="5000"
pin1=int(input("enter the PIN Value"))
balance=int(input("enter the amount want "))
if pin == pin1:
    print("Enter Amount")
elif balance < 5000:
    print("successful withdraw the amount")
else :
    print("insufficient Balance")