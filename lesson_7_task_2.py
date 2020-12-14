from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, var):
        self.var = var

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
     @property
     def calculate(self):
         return (self.var / 6.5) + 0.5


class Suit(Clothes):
     @property
     def calculate(self):
         return (2 * self.var) + 0.3


coat = Coat(38)
suit = Suit(186)
print(coat.calculate)
print(suit.calculate)
