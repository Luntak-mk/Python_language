'''
Задание №5.
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
'''

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'{self.title} производит заполнение документов')
class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} производит редактирование документов')
class Handle(Stationery):
    def draw(self):
        print(f'{self.title} производит выделение элементов документов')

my_pen = Pen('Ручка Bic')
my_pen.draw()
my_pencil = Pencil('Карандаш KOH-I-NOOR')
my_pencil.draw()

my_handle = Handle('Маркер ErichKrause')
my_handle.draw()