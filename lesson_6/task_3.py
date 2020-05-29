'''
Задание №3.
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        return f'Полное имя сотрудника {self.name} {self.surname} и должность {self.position}'
    def get_total_icome(self):
        return self._incom['wage'] + self._incom['bonus']


my_position = Position('Denis', 'Ovlasyuk', 'Manager', 35000, 25000)
print(my_position.name)
print(my_position.surname)
print(my_position.position)
print(my_position.get_full_name())
print(f'Доход сотрудника {my_position.get_total_icome()}')

my_position_1 = Position('Петр', 'Петров', 'Sale manager', 25000, 25000)
print(my_position_1.name)
print(my_position_1.surname)
print(my_position_1.position)
print(my_position_1.get_full_name())
print(f'Доход сотрудника {my_position_1.get_total_icome()}')
