def modify_int(x):
    x = x + 100
    print('Inside int function:', x)

def modify_list(lst):
    lst.append('mango')
    print('Inside list function:', lst)

num = 5
items = ['apple', 'banana']

modify_int(num)
print('After int function:', num)       # Line A

modify_list(items)
print('After list function:', items)    # Line B



# Line A output: _______________________________
# Line B output: _______________________________

# Explain in one sentence WHY Line A and Line B behave differently:

# ___________________________________________________________

# ___________________________________________________________
