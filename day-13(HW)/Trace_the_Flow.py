from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    def drive(self):
        print('Starting drive sequence...')
        self.start_engine()
        self._check_fuel()
        print('Now driving!')

    def _check_fuel(self):
        print('Fuel check: OK (Vehicle default)')


class Car(Vehicle):

    def start_engine(self):
        print('Car engine: VROOM!')


class ElectricCar(Car):

    def start_engine(self):
        super().start_engine()          # calls Car's start_engine
        print('Battery charged: 100%')

    def _check_fuel(self):
        print('Battery check: OK (ElectricCar override)')

    def __str__(self):
        return 'ElectricCar Object'


# Run this code:
c  = Car()
ec = ElectricCar()

print('--- Car.drive() ---')
c.drive()

print('--- ElectricCar.drive() ---')
ec.drive()

print('--- print(ec) ---')
print(ec)

# Write the expected output for each section:

Car.drive()
# Line 1: Starting drive sequence...
# Line 2: Car engine: VROOM!
# Line 3: Fuel check: OK (Vehicle default)
# Line 4: Now driving!

ElectricCar.drive() 
# Line 1: Starting drive sequence...
# Line 2: Car engine: VROOM!
# Line 3: Battery charged: 100%
# Line 4: Battery check: OK (ElectricCar override)
# Line 5: Now driving!

print(ec) 
# Output: ElectricCar Object
