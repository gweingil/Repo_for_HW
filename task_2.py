from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3

    def sum_consumtion (self, list_clothes):
        a = 0
        for clothes in list_clothes:
            a += clothes.consumption
            return a


coat = Coat(44)
suit_1 = Suit(1.55)
suit_2 = Suit(1.85)
suit_3 = Suit(1.56)
suit_4 = Suit(1.94)
list_suits = [suit_4, suit_3, suit_2, suit_1]
print(coat.consumption)
print(suit_1.consumption)
print(clothes.sum_consumption(list_suits))