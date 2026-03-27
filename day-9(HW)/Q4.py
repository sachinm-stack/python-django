def my_sum(*args):
    # return the sum of all values passed
    return sum(args)

def stats(*args):
    # print count, min, max, and average
    print("stat fuunct:")
    print ("count",len(args))
    print ("min",min(args))
    print ("max",max(args))
    print ("average",sum(args)/len(args))
# Test my_sum:
print(my_sum(10, 20))          # 30
print(my_sum(1, 2, 3, 4, 5))  # 15
print(my_sum(100))             # 100

# Test stats:
stats(5, 10, 15, 20, 25)
# Expected output:
# Count  : 5
# Min    : 5
# Max    : 25
# Average: 15.0
