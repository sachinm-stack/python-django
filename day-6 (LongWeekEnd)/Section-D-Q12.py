# Q12.break, continue & while..else


# PART A — Trace this code. Write the EXACT output:

for i in range(1, 11):
 if i % 3 == 0:
   continue
 if i == 8:
    break
 print(i, end=' ')

# Output: __1,2,4,5,7,_


# PART B — Fix the infinite loop (don't change the while condition):

i = 1
while i <= 5:
 print(i)
 i=i+1

# something is missing here

# PART C — Write a program using while..else:

# Ask the user to guess a secret word (hardcode it as 'python').
# Give them 3 attempts. If correct → break + print 'Correct!'
# If all 3 fail → else block prints 'The word was: python'

secret="python"
attempt=3
while attempt>0:
    guess =(input("guess the Word!"))
    if guess == secret:
        print("you Won!")
        break
    else :
        attempt -=1
        print("wrong!",attempt,"attempt left")
else:
    print("game over! Word was:",secret)
