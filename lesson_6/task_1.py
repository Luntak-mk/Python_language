'''
Задание №1.
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
import time
class TrafficLight:
    __color = ('Красный', 'Желтый', 'Зеленый')
    def running(self):
        while True:
            print(f'Горит {TrafficLight.__color[0]} цвет.')
            time.sleep(7)
            print(f'Горит {TrafficLight.__color[1]} цвет.')
            time.sleep(2)
            print(f'Горит {TrafficLight.__color[2]} цвет.')
            time.sleep(10)

my_traffic_light = TrafficLight()
my_traffic_light.running()