s={30,20,10}
print(s)
print(type(s))

s.add(40)
print(s)
s.update([50,60])
print(s)
s.remove(20)
print(s)
s.discard(2)
print(s)

s.pop()
print(s)

s.clear()
print(s)

a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

