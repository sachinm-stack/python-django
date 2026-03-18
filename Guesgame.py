import random
secret = random.randint(1,10)
guess=int(input("Guess thee number between 1 to 10 :"))
if guess == secret:
    print("congrats the num is correct!!")
else:
    print("sorry, the num was",secret)