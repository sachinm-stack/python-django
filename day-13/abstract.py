from abc import ABC, abstractmethod

class Animal(ABC):   # Abstract class

    @abstractmethod
    def sound(self):
        pass   # No implementation

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Usage
d = Dog()
c = Cat()

print(d.sound())   # Bark
print(c.sound())   # Meow