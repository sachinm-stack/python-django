alice_friends = {"bob","carol","dave","eve"} 
bob_friends = {"carol","frank","eve","grace"}

# //mutual friend:
print( alice_friends & bob_friends )
print (alice_friends.intersection(bob_friends))

#all unique ppl both frnd lists:
print(alice_friends ^ bob_friends)

#ppl alice but not bob's:
print(alice_friends - bob_friends)

#wheter dave is in bob's list:
print("dave" in bob_friends)