# Q11.Loop Patterns



# Pattern 1 — sum of 1 to 100 using a while loop
# Expected: Sum = 5050

i=1
total=0
while i<=100:
    total=total+i
    i=i+1
    print("sum:",total)



# Pattern 2 — print all numbers 1-50 divisible by both 3 AND 5
# Expected: 15 30 45

i=1
while i <= 50 :
  if i%5==0 and i%3==0:
    print(i)
  i =i+1


# Pattern 3 — countdown from 20, skip multiples of 4, stop at 0
# Expected: 20 19 18 17 15 14 13 11 10 9 7 6 5 3 2 1

i=20
while i > 0 :
  if i % 4 != 0 :
    print(i)
  i =i-1

# (16, 12, 8, 4 are skipped. Stop AT 0, don't print it.)

# Pattern 4 — number pyramid
# Expected:

i = 1

while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j = j + 1
    print()   # move to next line
    i = i + 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
