# Q9. Logical Operators — Predict the Flow
username = 'admin'
password = '1234'
secret = '7777'
# Scenario 1: user types admin / wrong / 7777
# Which line executes? __wrong pass_ Why? __bcause enter  wrong pass_
# Scenario 2: user types wrong / 1234 / 7777
# Which line executes? _user name wrong__ Why? ___
# Scenario 3: user types admin / 1234 / 7777
# Which line executes? __welcome_ Why? __ all correct _
# The code:
u = input('Username: ')
p = input('Password: ')
s = input('Secret: ')
if u == username and p == password and s == secret:
 print('Welcome!')
elif u != username:
 print('Wrong username')
elif p != password:
 print('Wrong password')
else:
 print('Wrong secret code')