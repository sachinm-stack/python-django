import random
secret=random.randint(1,10)
attempt=3
while attempt>0:
    guess =int(input("guess number 1-10:"))
    if guess == secret:
        print("you Won!")
        break
    else :
        attempt -=1
        print("wrong!",attempt,"attempt left")
else:
    print("game over! number was:",secret)