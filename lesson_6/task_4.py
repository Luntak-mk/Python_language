'''
Задание №4.
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
(TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Машина поехала.')
    def stop(self):
        print('Машина остановилась.')
    def turn(self, direction):
        if direction == 'налево':
            print('Машина повернула налево.')
        elif direction == 'направо':
            print('Машина повернула направо.')
    def show_speed(self):
        print(f'Скорость машины составляет {self.speed} км./ч.')

class TownCar(Car):
    def show_speed(self) :
        if self.speed > 60:
            print ( f'Скорость машины составляет {self.speed} км./ч. Внимание! '
                    f'Вы превысили скорость. Скорость машины должна быть не больше 60 км./ч.' )
class SportCar(Car):
    def __init__(self, speed, color, name, is_police, contest):
        super().__init__(speed, color, name, is_police)
        self.contest = contest
    def show_contest(self):
        print(f'Машина участвует в соревнованиях {self.contest}')

class WorkCar(Car):
    def show_speed(self) :
        if self.speed > 40:
            print(f'Скорость машины составляет {self.speed} км./ч. Внимание! '
                  f'Вы превысили скорость. Скорость машины должна быть не больше 60 км./ч.')

class PoliceCar(Car):
    def show_task(self, task):
        print('Машина выехала выполнять следующее задание:', task)

my_towncar = TownCar(70, 'black', 'Qashqai', False)
print(my_towncar.speed)
print(my_towncar.is_police)
print(my_towncar.color)
print(my_towncar.name)
my_towncar.go()
my_towncar.show_speed()
my_towncar.turn('налево')
my_towncar.stop()

my_sportcar = SportCar(220, 'black', 'Ford Fiesta Turbo', False, 'Ралли')
print(my_sportcar.speed)
print(my_sportcar.is_police)
print(my_sportcar.color)
print(my_sportcar.name)
my_sportcar.show_contest()
my_sportcar.go()
my_sportcar.show_speed()
my_sportcar.turn('налево')
my_sportcar.stop()

my_workcar = WorkCar(60, 'black', 'Kamaz', False)
print(my_workcar.speed)
print(my_workcar.is_police)
print(my_workcar.color)
print(my_workcar.name)
my_workcar.go()
my_workcar.show_speed()
my_workcar.turn('налево')
my_workcar.stop()

my_policecar = PoliceCar(150, 'white', 'Ford Focus', True)
print(my_policecar.speed)
print(my_policecar.is_police)
print(my_policecar.color)
print(my_policecar.name)
my_policecar.go()
my_policecar.show_speed()
my_policecar.turn('налево')
my_policecar.show_task('Патрулирование')
my_policecar.stop()