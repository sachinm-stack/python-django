def func(a,b):
    print(a)
    print(b)
    return(a+b)
c=func(2,3)
print(c)



def func(a=10,b=3):
    print(a)
    print(b)
    return a+b
c=func(20)
print("1111111111111111111",c)
c=func(5,20)
print("222222222222222",c)
c=func(b=20)
print("33333333333333333",c)



def fun():
    list=[1,2,3]
    list.append(100)
    return list
c=fun()
print(c)


def info(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs["name"])
    print(kwargs["age"])
info(name="kumar",age=12)


def add(*args):
    print(type(args))
    return sum(args)
print(add(1,2,3))
print(add(1,2,30,40,50))

