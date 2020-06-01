'''
Задание №2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def fabric_consumption(self):
        pass
    def __add__(self, other):
        return round(self.fabric_consumption() + other.fabric_consumption(), 2)

class Coat(Clothes):
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size == 'm':
            self._size = 46
        elif size == 'l':
            self._size = 48
        elif size == 'xl':
            self._size = 50
        return self._size

    def fabric_consumption(self):
        return round(self._size / 6.5 + 0.5, 2)

class Suit(Clothes):
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size >= 2:
            self._size = 1.95
        elif size <= 1:
            self._size = 1.2
        return self._size

    def fabric_consumption(self):
        return round(2 * self._size + 0.3, 2)


my_coat = Coat('m')
print('Размер пальто в цифрах:', my_coat.size)
print('Расчет требуемой ткани на производство одной единицы пальто', my_coat.fabric_consumption())

my_suit = Suit(5)
print('Рост костюма:', my_suit.size)
print('Расчет требуемой ткани на производство одного костюма', my_suit.fabric_consumption())

print(f'Суммарный расход ткани на производство одежды: {my_coat + my_suit}')