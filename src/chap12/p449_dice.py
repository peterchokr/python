# 주사위 클래스

from random import randint

class Dice :
    def __init__(self, x, y) :
       self._x = x
       self._y = y
       self._size = 30
       self._value = 1

    def read_dice(self) :
        return self._value

    def print_dice(self) :
        print("주사위의 값=", self._value)

    def roll_dice(self) :
        self._value = randint(1, 6)

d = Dice(100, 100)
d.roll_dice()
d.print_dice()