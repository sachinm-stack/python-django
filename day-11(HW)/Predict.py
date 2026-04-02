class Car:

    def __init__(self, brand, colour, speed):
        self.brand  = brand
        self.colour = colour
        self.speed  = speed

    def describe(self):
        print(f'{self.brand} — {self.colour} — {self.speed} kmph')

c1 = Car('Toyota', 'Red',  120)
c2 = Car('Honda',  'Blue', 150)
c3 = Car('BMW',    'Black', 200)

c1.describe()           # Line A
c2.describe()           # Line B
c3.describe()           # Line C

c1.colour = 'White'     # update an attribute
c1.describe()           # Line D

print(type(c1))         # Line E
print(id(c1) == id(c2)) # Line F





# Line A: ____Toyota — Red — 120 kmph_____
# Line B: `____ Honda — Blue — 150 kmph_______`
# Line C: ____BMW — Black — 200 kmph_______
# Line D: ___________ c1.colour = 'White'____
# Line E: __________ <class '__main__.Car'>_____________________
# Line F: ______________ False_________________
